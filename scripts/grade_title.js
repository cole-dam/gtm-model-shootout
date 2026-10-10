// Grader for the title-normalization task.
// Promptfoo calls this once per answer. It returns pass/fail plus a reason.
// Scoring: 1 point if both fields match, 0.5 if one matches, 0 if neither.

module.exports = (output, context) => {
  const vars = context.vars;
  let text = String(output || '');

  // Local models sometimes think out loud or wrap JSON in code fences.
  // Take the last JSON object, which is the final answer after that reasoning.
  text = text.replace(/<think>[\s\S]*?<\/think>/gi, '');
  text = text.replace(/```(?:json)?/gi, '');
  const candidates = text.match(/\{[^{}]*\}/g);
  if (!candidates) {
    return { pass: false, score: 0, reason: 'No JSON found in answer' };
  }

  let parsed = null;
  for (let i = candidates.length - 1; i >= 0; i--) {
    try {
      const obj = JSON.parse(candidates[i]);
      if (obj && (Object.prototype.hasOwnProperty.call(obj, 'function') || Object.prototype.hasOwnProperty.call(obj, 'seniority'))) {
        parsed = obj;
        break;
      }
    } catch (e) {
      // Keep looking. An earlier brace may be a scrap from the reasoning.
    }
  }
  if (!parsed) {
    return { pass: false, score: 0, reason: 'Answer was not valid JSON' };
  }

  const norm = (s) => String(s || '').trim().toLowerCase();
  // An answer-key cell can list several acceptable answers separated by "|".
  const accepts = (answer, key) =>
    String(key || '').split('|').map(norm).includes(norm(answer));
  const fnOk = accepts(parsed.function, vars.expected_function);
  const senOk = accepts(parsed.seniority, vars.expected_seniority);
  const score = (fnOk ? 0.5 : 0) + (senOk ? 0.5 : 0);

  const misses = [];
  if (!fnOk) misses.push(`function: got "${parsed.function}", wanted "${vars.expected_function}"`);
  if (!senOk) misses.push(`seniority: got "${parsed.seniority}", wanted "${vars.expected_seniority}"`);

  return {
    pass: fnOk && senOk,
    score,
    reason: misses.length ? misses.join('; ') : 'Both fields correct',
  };
};
