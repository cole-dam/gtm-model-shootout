# GTM Model Shootout: Title Normalization
_Run on 2026-10-10 · 25 job titles_

| Model | Got it fully right | Partial credit score | Avg speed | Cost for this run | Cost per 10k titles | Verdict |
|---|---|---|---|---|---|---|
| Qwen 3.8 Max (hosted) | 25/25 (100%) | 100% | 0.0s | $0.0324 | $12.96 | ✅ Production-ready |
| Claude Haiku 5.5 | 25/25 (100%) | 100% | 0.0s | $0.0021 | $0.83 | ✅ Production-ready |
| Qwen 3.8 27B (local) | 25/25 (100%) | 100% | 9.1s | Free (local) | Free (local) | ✅ Production-ready |
| Gemini 3.8 Flash | 25/25 (100%) | 100% | 0.0s | $0.0286 | $11.44 | ✅ Production-ready |
| GLM 5.3 | 25/25 (100%) | 100% | 0.0s | $0.0036 | $1.44 | ✅ Production-ready |
| Kimi K3 | 25/25 (100%) | 100% | 0.0s | $0.0640 | $25.58 | ✅ Production-ready |
| DeepSeek V4 Flash | 25/25 (100%) | 100% | 0.0s | $0.0016 | $0.65 | ✅ Production-ready |
| Claude Sonnet 5.5 | 24/25 (96%) | 98% | 0.0s | $0.0381 | $15.26 | ✅ Production-ready |
| Jev (with rules) | 24/25 (96%) | 98% | 0.1s | $0.0008 | $0.30 | ✅ Production-ready |
| Jev (title only) | 16/25 (64%) | 80% | 0.1s | $0.0004 | $0.17 | 🟠 Needs human review |

## Who served each answer

OpenRouter can send the same model ID to different hosts. If one model shows several hosts, treat its score as a mix until you pin a host.

- **Qwen 3.8 Max (hosted)**: Alibaba (25)
- **Claude Haiku 5.5**: Claude Platform on AWS (25)
- **Qwen 3.8 27B (local)**: LM Studio (25)
- **Gemini 3.8 Flash**: Google (25)
- **GLM 5.3**: Wafer (9)
- **Kimi K3**: DeepInfra (8)
- **DeepSeek V4 Flash**: CoreWeave (10)
- **Claude Sonnet 5.5**: Claude Platform on AWS (25)
- **Jev (with rules)**: not recorded
- **Jev (title only)**: not recorded

## Where each model slipped

**Qwen 3.8 Max (hosted)**: no misses 🎯

**Claude Haiku 5.5**: no misses 🎯

**Qwen 3.8 27B (local)**: no misses 🎯

**Gemini 3.8 Flash**: no misses 🎯

**GLM 5.3**: no misses 🎯

**Kimi K3**: no misses 🎯

**DeepSeek V4 Flash**: no misses 🎯

**Claude Sonnet 5.5**: 1 misses
- Sales Operations Manager → seniority: got "Manager", wanted "IC"

**Jev (with rules)**: 1 misses
- Sales Operations Manager → seniority: got "Manager", wanted "IC"

**Jev (title only)**: 9 misses
- Content Marketing Manager → seniority: got "Manager", wanted "IC"
- Partner Marketing Manager → seniority: got "Manager", wanted "IC"
- Product Marketing Manager → seniority: got "Manager", wanted "IC"
- Senior Product Manager → seniority: got "Manager", wanted "IC"
- Sales Operations Manager → function: got "Sales", wanted "Operations"; seniority: got "Manager", wanted "IC"
- Key Account Manager → seniority: got "Manager", wanted "IC"
- Marketing Operations Specialist → function: got "Marketing", wanted "Operations"
- Customer Onboarding Manager → seniority: got "Manager", wanted "IC"
- Director of Sales Operations → function: got "Sales", wanted "Operations"

## How to read this
- **Got it fully right**: both department and seniority matched the answer key.
- **Partial credit**: half a point for each field. Useful for spotting "close but not quite."
- **Verdict** is based on partial credit. Local speed depends on your Mac, not the model alone.
- **Cost** is what OpenRouter reported for these calls. It does not include the 5.5% fee charged when you buy credits.
- **Reasoning tokens** are hidden thinking. They raise cost and time even when the visible answer is one line of JSON.
