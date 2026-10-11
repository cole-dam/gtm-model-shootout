# GTM Model Shootout: Title Normalization
_Run on 2026-10-10 · 26 job titles_

| Model | Got it fully right | Partial credit score | Avg speed | Cost for this run | Cost per 10k titles | Verdict |
|---|---|---|---|---|---|---|
| Claude Haiku 5.5 | 26/26 (100%) | 100% | 1.5s | $0.0023 | $0.88 | ✅ Production-ready |
| Claude Sonnet 5.5 | 26/26 (100%) | 100% | 2.4s | $0.0432 | $16.62 | ✅ Production-ready |
| GLM 5.3 | 26/26 (100%) | 100% | 0.6s | $0.0038 | $1.48 | ✅ Production-ready |
| Gemini 3.8 Flash | 26/26 (100%) | 100% | 2.7s | $0.0284 | $10.94 | ✅ Production-ready |
| Kimi K3 | 26/26 (100%) | 100% | 1.8s | $0.0721 | $27.72 | ✅ Production-ready |
| DeepSeek V4 Flash | 26/26 (100%) | 100% | 0.8s | $0.0017 | $0.67 | ✅ Production-ready |
| Qwen 3.8 Max (hosted) | 25/26 (96%) | 98% | 5.5s | $0.0399 | $15.36 | ✅ Production-ready |
| Qwen 3.8 27B (local) | 25/26 (96%) | 98% | 8.9s | Free (local) | Free (local) | ✅ Production-ready |

## Who served each answer

OpenRouter can send the same model ID to different hosts. If one model shows several hosts, treat its score as a mix until you pin a host.

- **Claude Haiku 5.5**: Claude Platform on AWS (26) · reasoning tokens: 1126
- **Claude Sonnet 5.5**: Claude Platform on AWS (26) · reasoning tokens: 817
- **GLM 5.3**: Wafer (26) · reasoning tokens: 95
- **Gemini 3.8 Flash**: Google (26) · reasoning tokens: 5426
- **Kimi K3**: DeepInfra (26) · reasoning tokens: 2197
- **DeepSeek V4 Flash**: CoreWeave (26) · reasoning tokens: 1871
- **Qwen 3.8 Max (hosted)**: Alibaba (26) · reasoning tokens: 2655
- **Qwen 3.8 27B (local)**: LM Studio (26) · reasoning tokens: 3527

## Where each model slipped

**Claude Haiku 5.5**: no misses 🎯

**Claude Sonnet 5.5**: no misses 🎯

**GLM 5.3**: no misses 🎯

**Gemini 3.8 Flash**: no misses 🎯

**Kimi K3**: no misses 🎯

**DeepSeek V4 Flash**: no misses 🎯

**Qwen 3.8 Max (hosted)**: 1 misses
- Controller → seniority: got "Manager", wanted "Director"

**Qwen 3.8 27B (local)**: 1 misses
- Controller → seniority: got "IC", wanted "Director"

## How to read this
- **Got it fully right**: both department and seniority matched the answer key.
- **Partial credit**: half a point for each field. Useful for spotting "close but not quite."
- **Verdict** is based on partial credit. Local speed depends on your Mac, not the model alone.
- **Cost** is what OpenRouter reported for these calls. It does not include the 5.5% fee charged when you buy credits.
- **Reasoning tokens** are hidden thinking. They raise cost and time even when the visible answer is one line of JSON.
