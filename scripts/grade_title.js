// Grader for the title-normalization task.
// Promptfoo calls this once per answer. It returns pass/fail plus a reason.
// Scoring: 1 point if both fields match, 0.5 if one matches, 0 if neither.

module.exports = (output, context) => {
  const vars = context.vars;
  let text = String(output || '');

  // Local models sometimes "think out loud" or wrap JSON in code fences. Strip that.
  text = text.replace(/<think>[\s\S]*?<\/think>/gi, '');
  const match = text.match(/\{[\s\S]*\}/);
  if (!match) {
    return { pass: false, score: 0, reason: 'No JSON found in answer' };
  }

  let parsed;
  try {
    parsed = JSON.parse(match[0]);
  } catch (e) {
    return { pass: false, score: 0, reason: 'Answer was not valid JSON' };
  }

  const norm = (s) => String(s || '').trim().toLowerCase();
  const fnOk = norm(parsed.function) === norm(vars.expected_function);
  const senOk = norm(parsed.seniority) === norm(vars.expected_seniority);
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
