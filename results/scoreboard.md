# GTM Model Shootout: Title Normalization
_Run on 2026-10-10 · 26 job titles_

| Model | Got it fully right | Partial credit score | Avg speed | Cost for this run | Cost per 10k titles | Verdict |
|---|---|---|---|---|---|---|
| Claude Haiku 5.5 | 26/26 (100%) | 100% | 0.0s | $0.0023 | $0.88 | ✅ Production-ready |
| Claude Sonnet 5.5 | 26/26 (100%) | 100% | 0.0s | $0.0432 | $16.62 | ✅ Production-ready |
| Gemini 3.8 Flash | 26/26 (100%) | 100% | 0.0s | $0.0284 | $10.94 | ✅ Production-ready |
| GLM 5.3 | 26/26 (100%) | 100% | 0.0s | $0.0038 | $1.48 | ✅ Production-ready |
| Kimi K3 | 26/26 (100%) | 100% | 0.0s | $0.0721 | $27.72 | ✅ Production-ready |
| DeepSeek V4 Flash | 26/26 (100%) | 100% | 0.0s | $0.0017 | $0.67 | ✅ Production-ready |
| Jev (with rules) | 26/26 (100%) | 100% | 0.1s | $0.0008 | $0.30 | ✅ Production-ready |
| Qwen 3.8 Max (hosted) | 25/26 (96%) | 98% | 0.0s | $0.0399 | $15.36 | ✅ Production-ready |
| Qwen 3.8 27B (local) | 25/26 (96%) | 98% | 8.9s | Free (local) | Free (local) | ✅ Production-ready |
| Jev (title only) | 19/26 (73%) | 87% | 0.1s | $0.0004 | $0.17 | 🟡 Good with spot checks |

## Who served each answer

OpenRouter can send the same model ID to different hosts. If one model shows several hosts, treat its score as a mix until you pin a host.

- **Claude Haiku 5.5**: Claude Platform on AWS (26)
- **Claude Sonnet 5.5**: Claude Platform on AWS (26)
- **Gemini 3.8 Flash**: Google (26)
- **GLM 5.3**: not recorded
- **Kimi K3**: not recorded
- **DeepSeek V4 Flash**: not recorded
- **Jev (with rules)**: not recorded
- **Qwen 3.8 Max (hosted)**: Alibaba (26)
- **Qwen 3.8 27B (local)**: LM Studio (26)
- **Jev (title only)**: not recorded

## Where each model slipped

**Claude Haiku 5.5**: no misses 🎯

**Claude Sonnet 5.5**: no misses 🎯

**Gemini 3.8 Flash**: no misses 🎯

**GLM 5.3**: no misses 🎯

**Kimi K3**: no misses 🎯

**DeepSeek V4 Flash**: no misses 🎯

**Jev (with rules)**: no misses 🎯

**Qwen 3.8 Max (hosted)**: 1 misses
- Controller → seniority: got "Manager", wanted "Director"

**Qwen 3.8 27B (local)**: 1 misses
- Controller → seniority: got "IC", wanted "Director"

**Jev (title only)**: 7 misses
- Customer Success Manager → seniority: got "Manager", wanted "IC"
- Chief Revenue Officer → function: got "Executive", wanted "Sales"
- RevOps Manager → seniority: got "Manager", wanted "IC"
- Lifecycle Marketing Manager → seniority: got "Manager", wanted "IC"
- Product Manager II → seniority: got "Manager", wanted "IC"
- Marketing Ops Team Lead → function: got "Marketing", wanted "Operations"
- Demand Gen Manager → seniority: got "Manager", wanted "IC"

## How to read this
- **Got it fully right**: both department and seniority matched the answer key.
- **Partial credit**: half a point for each field. Useful for spotting "close but not quite."
- **Verdict** is based on partial credit. Local speed depends on your Mac, not the model alone.
- **Cost** is what OpenRouter reported for these calls. It does not include the 5.5% fee charged when you buy credits.
- **Reasoning tokens** are hidden thinking. They raise cost and time even when the visible answer is one line of JSON.
