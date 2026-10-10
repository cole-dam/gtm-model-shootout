# GTM Model Shootout: Title Normalization
_Run on 2026-10-10 · 26 job titles_

| Model | Got it fully right | Partial credit score | Avg speed | Cost for this run | Cost per 10k titles | Verdict |
|---|---|---|---|---|---|---|
| Claude Sonnet 5.5 | 26/26 (100%) | 100% | 2.1s | $0.0356 | $13.69 | ✅ Production-ready |
| Claude Haiku 5.5 | 26/26 (100%) | 100% | 1.5s | $0.0019 | $0.72 | ✅ Production-ready |
| Qwen 3.8 Max (hosted) | 26/26 (100%) | 100% | 4.4s | $0.0352 | $13.55 | ✅ Production-ready |
| GLM 5.3 | 26/26 (100%) | 100% | 1.7s | $0.0094 | $3.61 | ✅ Production-ready |
| Gemini 3.8 Flash | 26/26 (100%) | 100% | 2.4s | $0.0296 | $11.38 | ✅ Production-ready |
| DeepSeek V4 Flash | 26/26 (100%) | 100% | 1.3s | $0.0019 | $0.73 | ✅ Production-ready |
| Kimi K3 | 26/26 (100%) | 100% | 2.4s | $0.0509 | $19.59 | ✅ Production-ready |
| Qwen 3.8 27B (local) | 25/26 (96%) | 96% | 13.6s | Free (local) | Free (local) | ✅ Production-ready |

## Who served each answer

OpenRouter can send the same model ID to different hosts. If one model shows several hosts, treat its score as a mix until you pin a host.

- **Claude Sonnet 5.5**: Claude Platform on AWS (26) · reasoning tokens: 485
- **Claude Haiku 5.5**: Claude Platform on AWS (26) · reasoning tokens: 777
- **Qwen 3.8 Max (hosted)**: Alibaba (26) · reasoning tokens: 2384
- **GLM 5.3**: Inceptron (25), Wafer (1) · reasoning tokens: 2575
- **Gemini 3.8 Flash**: Google (26) · reasoning tokens: 6058
- **DeepSeek V4 Flash**: Cohere (26) · reasoning tokens: 1782
- **Kimi K3**: Wafer (26) · reasoning tokens: 2594
- **Qwen 3.8 27B (local)**: LM Studio (26) · reasoning tokens: 5048

## Where each model slipped

**Claude Sonnet 5.5**: no misses 🎯

**Claude Haiku 5.5**: no misses 🎯

**Qwen 3.8 Max (hosted)**: no misses 🎯

**GLM 5.3**: no misses 🎯

**Gemini 3.8 Flash**: no misses 🎯

**DeepSeek V4 Flash**: no misses 🎯

**Kimi K3**: no misses 🎯

**Qwen 3.8 27B (local)**: 1 misses
- Controller → No JSON found in answer

## How to read this
- **Got it fully right**: both department and seniority matched the answer key.
- **Partial credit**: half a point for each field. Useful for spotting "close but not quite."
- **Verdict** is based on partial credit. Local speed depends on your Mac, not the model alone.
- **Cost** is what OpenRouter reported for these calls. It does not include the 5.5% fee charged when you buy credits.
- **Reasoning tokens** are hidden thinking. They raise cost and time even when the visible answer is one line of JSON.
