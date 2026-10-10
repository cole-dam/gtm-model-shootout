# GTM Model Shootout: Title Normalization
_Run on 2026-10-10 · 25 job titles_

| Model | Got it fully right | Partial credit score | Avg speed | Cost for this run | Cost per 10k titles | Verdict |
|---|---|---|---|---|---|---|
| Claude Sonnet 5.5 | 24/25 (96%) | 98% | 1.7s | $0.0264 | $10.55 | ✅ Production-ready |
| Gemini 3.8 Flash | 24/25 (96%) | 98% | 3.3s | $0.0344 | $13.77 | ✅ Production-ready |
| GLM 5.3 | 24/25 (96%) | 98% | 1.3s | $0.0098 | $3.93 | ✅ Production-ready |
| Kimi K3 | 24/25 (96%) | 98% | 3.4s | $0.0498 | $19.93 | ✅ Production-ready |
| Claude Haiku 5.5 | 23/25 (92%) | 96% | 1.5s | $0.0016 | $0.65 | ✅ Production-ready |
| Qwen 3.8 27B (local) | 23/25 (92%) | 96% | 9.8s | Free (local) | Free (local) | ✅ Production-ready |
| DeepSeek V4 Flash | 23/25 (92%) | 96% | 1.3s | $0.0014 | $0.56 | ✅ Production-ready |
| Qwen 3.8 Max (hosted) | 22/25 (88%) | 94% | 5.2s | $0.0320 | $12.79 | 🟡 Good with spot checks |

## Who served each answer

OpenRouter can send the same model ID to different hosts. If one model shows several hosts, treat its score as a mix until you pin a host.

- **Claude Sonnet 5.5**: not recorded · reasoning tokens: 189
- **Gemini 3.8 Flash**: not recorded · reasoning tokens: 7706
- **GLM 5.3**: not recorded · reasoning tokens: 1493
- **Kimi K3**: not recorded · reasoning tokens: 2095
- **Claude Haiku 5.5**: not recorded · reasoning tokens: 795
- **Qwen 3.8 27B (local)**: not recorded · reasoning tokens: 2879
- **DeepSeek V4 Flash**: not recorded · reasoning tokens: 1355
- **Qwen 3.8 Max (hosted)**: not recorded · reasoning tokens: 2470

## Where each model slipped

**Claude Sonnet 5.5**: 1 misses
- Controller → seniority: got "Manager", wanted "Director"

**Gemini 3.8 Flash**: 1 misses
- Customer Success Manager → seniority: got "Manager", wanted "IC"

**GLM 5.3**: 1 misses
- Customer Success Manager → seniority: got "Manager", wanted "IC"

**Kimi K3**: 1 misses
- Customer Success Manager → seniority: got "Manager", wanted "IC"

**Claude Haiku 5.5**: 2 misses
- Group Product Manager → seniority: got "Director", wanted "Manager"
- Customer Success Manager → seniority: got "Manager", wanted "IC"

**Qwen 3.8 27B (local)**: 2 misses
- Product Manager II → seniority: got "Manager", wanted "IC"
- Customer Success Manager → seniority: got "Manager", wanted "IC"

**DeepSeek V4 Flash**: 2 misses
- Group Product Manager → seniority: got "IC", wanted "Manager"
- Customer Success Manager → seniority: got "Manager", wanted "IC"

**Qwen 3.8 Max (hosted)**: 3 misses
- Product Manager II → seniority: got "Manager", wanted "IC"
- Controller → seniority: got "Manager", wanted "Director"
- Customer Success Manager → seniority: got "Manager", wanted "IC"

## How to read this
- **Got it fully right**: both department and seniority matched the answer key.
- **Partial credit**: half a point for each field. Useful for spotting "close but not quite."
- **Verdict** is based on partial credit. Local speed depends on your Mac, not the model alone.
- **Cost** is what OpenRouter reported for these calls. It does not include the 5.5% fee charged when you buy credits.
- **Reasoning tokens** are hidden thinking. They raise cost and time even when the visible answer is one line of JSON.
