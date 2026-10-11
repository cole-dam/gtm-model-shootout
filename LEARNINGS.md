# Learnings: GTM Model Shootout

_Task 1 (job title normalization), October 10, 2026_

## The question

Can cheap and local AI models handle real go-to-market data work as well as expensive frontier models? Task 1 tested one of the most common GTM data jobs: turning messy job titles into a clean department and seniority level.

## Results

8 models, 26 practice titles, and 25 holdout titles the prompt was never tuned on.

| Model | Practice (26) | Holdout (25) | Cost per 10k titles |
|---|---|---|---|
| DeepSeek V4 Flash | 100% | 100% | $0.67 |
| Claude Haiku 5.5 | 100% | 100% | $0.88 |
| GLM 5.3 | 100% | 100% | $1.48 |
| Gemini 3.8 Flash | 100% | 100% | $10.94 |
| Kimi K3 | 100% | 100% | $27.72 |
| Qwen 3.8 Max (hosted) | 96% | 100% | $15.36 |
| Qwen 3.8 27B (local, Mac Studio) | 96% | 100% | Free (~9s per title) |
| Claude Sonnet 5.5 | 100% | 96% | $16.62 |

## What we found

| Finding | Evidence |
|---|---|
| **Cheap models match expensive ones on rule-based classification** | DeepSeek, Haiku, and GLM scored 100% on both sets for under $1.50 per 10k titles. Kimi K3 did the same work for ~40x the price. |
| **Instructions matter more than the model** | Scores went from scattered misses to near-perfect once clear seniority rules existed. |
| **Local is accurate but slow** | Qwen 27B on a Mac Studio hit 100% on the holdout for free, at ~9 seconds per title. 10k titles takes about a day. |
| **Bigger isn't automatically better** | Sonnet was the only model to miss on the holdout. Qwen Max lost to its smaller sibling on practice. |

**The takeaway:** for GTM data work, spend the effort on the rules and the answer key, then use the cheapest model that passes.

## What we learned about evals

| Lesson | What happened |
|---|---|
| **When most models "miss," check the answer key first** | Six of eight models called a Controller a Director. They were right; the key was wrong. |
| **Only grade what the instructions define** | "CX Ops" can reasonably be Support, Success, or Ops depending on the company. Grading it one way was unfair, so it was cut. |
| **Make tests fair with rules, not loose grading** | Accepting "IC or Manager" for Customer Success Manager would have hidden a real, costly error. Adding an explicit rule kept the test meaningful. |
| **Hold out an exam you never tune on** | Every prompt fix came from practice misses. The holdout proved the rules generalize instead of memorizing the practice titles. |
| **Realistic data beats clean data** | "CSM Manager" isn't a real title; "Manager, Customer Success" is, and it exposed a gap in the rules. Holdout titles include real-world noise like pipes, "@ Company," and hiring tags. |

The pattern under all of it: **the domain expert writing the answer key is the bottleneck, not the model.** Every meaningful improvement came from GTM judgment, not from switching models.

## The rules that made it work

The biggest unlock was a GTM-specific definition of "Manager":

- **"Manager" of a thing** (an account, channel, product, campaign, or function) is an **IC**: Account Manager, Product Manager, Lifecycle Marketing Manager, RevOps Manager.
- **"Manager" of a team of people** is a **people manager**: SDR Manager, Engineering Manager.
- **"Manager," first** ("Manager, Customer Success") is a **people manager**.

Most enrichment tools bucket every "Manager" title together by default. For persona targeting and buying committees, that's the wrong call: a Lifecycle Marketing Manager is a champion, not a budget owner.

## Setup

- **Eval engine:** [Promptfoo](https://promptfoo.dev), with a custom grader and a plain-English scoreboard
- **Hosted models:** OpenRouter (one API key for 7 models)
- **Local model:** Qwen 3.8 27B via LM Studio on a Mac Studio
- **Data:** 100% synthetic. No company or customer data.

## Next

Task 1 is saturated: every model scores 96–100%, so it can no longer rank them. The next tasks ladder up in difficulty to find where models actually separate.
