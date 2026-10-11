// Promptfoo custom provider for Jev (TypeSafe AI's "System One" decision model).
// Jev doesn't read a chat prompt. It gets a "state" (the job title) plus typed
// multiple-choice questions, and returns a choice and a confidence for each.
//
// config.includeRules = true  -> each answer option carries the prompt's rules in its description
// config.includeRules = false -> bare option names only (title-only baseline)
//
// The rules below mirror prompts/title_normalization.txt. Keep them in sync,
// and never add knowledge the LLMs' prompt doesn't have.

const fs = require('fs');
const path = require('path');

const PRICE_PER_INPUT_TOKEN = 0.042 / 1e6; // USD, published price; output tokens are free

function loadKey() {
  if (process.env.TYPESAFE_API_KEY) return process.env.TYPESAFE_API_KEY;
  try {
    const env = fs.readFileSync(path.join(__dirname, '..', '.env'), 'utf8');
    const m = env.match(/^TYPESAFE_API_KEY=(.+)$/m);
    if (m) return m[1].trim();
  } catch (e) {}
  return null;
}

const FUNCTIONS_WITH_RULES = {
  'Sales': 'Sales roles. Account Managers belong to Sales.',
  'Marketing': 'Marketing roles.',
  'Customer Support': 'Customer support roles.',
  'Customer Success': 'Customer success roles, including onboarding of existing customers.',
  'Engineering': 'Engineering roles.',
  'Product': 'Product roles.',
  'Operations': 'Revenue Operations, Sales Operations, and Marketing Operations roles.',
  'Finance': 'Finance roles.',
  'People': 'People and HR roles.',
  'Executive': 'Founders and CEOs, even if they also hold another title (e.g. Co-Founder & CMO). Other Chief officers take the department they name instead (e.g. CMO = Marketing, CRO = Sales).',
};

const SENIORITY_WITH_RULES = {
  'IC': 'Individual contributor. Includes titles where "Manager" names something the person owns, like an account, channel, product, campaign, or function (e.g. Account Manager, Product Manager, Campaign Manager).',
  'Manager': 'Manages a team of people. Includes Team Leads and Supervisors, titles where "Manager" names a team of people (e.g. SDR Manager, Engineering Manager), and titles starting with "Manager," followed by a team or department (e.g. "Manager, Sales Development").',
  'Director': 'Director level. "Head of X" counts as Director unless the title says VP or Chief.',
  'VP': 'Vice President level.',
  'C-Level': 'Founders, CEOs, and Chief officers.',
};

function bare(obj) {
  return Object.fromEntries(Object.keys(obj).map((k) => [k, null]));
}

class JevProvider {
  constructor(options = {}) {
    this.options = options;
    this.config = options.config || {};
    this.providerId = options.id || 'jev';
    this.label = options.label;
  }

  id() {
    return this.providerId;
  }

  async callApi(prompt, context) {
    const key = loadKey();
    if (!key) return { error: 'TYPESAFE_API_KEY is missing from .env' };

    const title = context?.vars?.title;
    if (!title) return { error: 'No {{title}} variable in this test' };

    const rules = this.config.includeRules !== false;
    const body = {
      model: this.config.model || 'jev-latest',
      state: `Job title: ${title}`,
      questions: {
        function: {
          type: 'choice',
          instructions: 'Which department this job title belongs to',
          criteria: rules ? FUNCTIONS_WITH_RULES : bare(FUNCTIONS_WITH_RULES),
        },
        seniority: {
          type: 'choice',
          instructions: 'The seniority level of this job title',
          criteria: rules ? SENIORITY_WITH_RULES : bare(SENIORITY_WITH_RULES),
        },
      },
    };

    const started = Date.now();
    let res, data;
    try {
      res = await fetch('https://api.typesafe.ai/v1/systemone', {
        method: 'POST',
        headers: { Authorization: `Bearer ${key}`, 'Content-Type': 'application/json' },
        body: JSON.stringify(body),
      });
      data = await res.json();
    } catch (e) {
      return { error: `Jev request failed: ${e.message}` };
    }
    if (!res.ok) return { error: `Jev API ${res.status}: ${JSON.stringify(data).slice(0, 300)}` };

    const fn = data.answers?.function || {};
    const sen = data.answers?.seniority || {};
    const inputTokens = data.usage?.input_tokens || 0;
    const outputTokens = data.usage?.output_tokens || 0;

    return {
      // Same JSON shape the LLMs return, so the existing grader works unchanged.
      output: JSON.stringify({ function: fn.choice, seniority: sen.choice }),
      tokenUsage: { prompt: inputTokens, completion: outputTokens, total: inputTokens + outputTokens },
      cost: inputTokens * PRICE_PER_INPUT_TOKEN,
      metadata: {
        jevModel: data.model,
        jevLatencyMs: Date.now() - started,
        functionConfidence: fn.confidence,
        seniorityConfidence: sen.confidence,
        functionProbabilities: fn.probabilities,
        seniorityProbabilities: sen.probabilities,
        requestId: res.headers.get('x-typesafe-request-id'),
      },
    };
  }
}

module.exports = JevProvider;
