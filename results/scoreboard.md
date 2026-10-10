# GTM Model Shootout: Title Normalization
_Run on 2026-10-10 · 25 job titles_

| Model | Got it fully right | Partial credit score | Avg speed | Cost for this run | Cost per 10k titles | Verdict |
|---|---|---|---|---|---|---|
| Claude Sonnet 5.5 | 24/25 (96%) | 98% | 1.8s | $0.0293 | $11.71 | ✅ Production-ready |
| Qwen 3.8 Max (hosted) | 24/25 (96%) | 98% | 5.4s | $0.0340 | $13.61 | ✅ Production-ready |
| Gemini 3.8 Flash | 24/25 (96%) | 98% | 3.4s | $0.0355 | $14.20 | ✅ Production-ready |
| GLM 5.3 | 24/25 (96%) | 98% | 1.4s | $0.0101 | $4.03 | ✅ Production-ready |
| Kimi K3 | 24/25 (96%) | 98% | 3.4s | $0.0503 | $20.12 | ✅ Production-ready |
| Claude Haiku 5.5 | 23/25 (92%) | 96% | 1.5s | $0.0017 | $0.68 | ✅ Production-ready |
| Qwen 3.8 27B (local) | 23/25 (92%) | 96% | 10.6s | Free (local) | Free (local) | ✅ Production-ready |
| DeepSeek V4 Flash | 23/25 (92%) | 96% | 1.4s | $0.0014 | $0.57 | ✅ Production-ready |

## Who served each answer

OpenRouter can send the same model ID to different hosts. If one model shows several hosts, treat its score as a mix until you pin a host.

- **Claude Sonnet 5.5**: not recorded · reasoning tokens: 468
- **Qwen 3.8 Max (hosted)**: not recorded · reasoning tokens: 2800
- **Gemini 3.8 Flash**: not recorded · reasoning tokens: 7995
- **GLM 5.3**: not recorded · reasoning tokens: 1550
- **Kimi K3**: not recorded · reasoning tokens: 2261
- **Claude Haiku 5.5**: not recorded · reasoning tokens: 945
- **Qwen 3.8 27B (local)**: not recorded · reasoning tokens: 3217
- **DeepSeek V4 Flash**: not recorded · reasoning tokens: 1451

## Where each model slipped

**Claude Sonnet 5.5**: 1 misses
- Sr. Dir. CX Ops → function: got "Operations", wanted "Customer Support"

**Qwen 3.8 Max (hosted)**: 1 misses
- Product Manager II → seniority: got "Manager", wanted "IC"

**Gemini 3.8 Flash**: 1 misses
- Controller → seniority: got "Director", wanted "Manager"

**GLM 5.3**: 1 misses
- Controller → seniority: got "Director", wanted "Manager"

**Kimi K3**: 1 misses
- Controller → seniority: got "Director", wanted "Manager"

**Claude Haiku 5.5**: 2 misses
- Controller → seniority: got "Director", wanted "Manager"
- Group Product Manager → seniority: got "Director", wanted "Manager"

**Qwen 3.8 27B (local)**: 2 misses
- Product Manager II → seniority: got "Manager", wanted "IC"
- Controller → seniority: got "Director", wanted "Manager"

**DeepSeek V4 Flash**: 2 misses
- Controller → seniority: got "Director", wanted "Manager"
- Group Product Manager → seniority: got "IC", wanted "Manager"

## How to read this
- **Got it fully right**: both department and seniority matched the answer key.
- **Partial credit**: half a point for each field. Useful for spotting "close but not quite."
- **Verdict** is based on partial credit. Local speed depends on your Mac, not the model alone.
- **Cost** is what OpenRouter reported for these calls. It does not include the 5.5% fee charged when you buy credits.
- **Reasoning tokens** are hidden thinking. They raise cost and time even when the visible answer is one line of JSON.
