# GTM Model Shootout: Title Normalization
_Run on 2026-10-10 · 25 job titles_

| Model | Got it fully right | Partial credit score | Avg speed | Cost for this run | Cost per 10k titles | Verdict |
|---|---|---|---|---|---|---|
| Claude Haiku 5.5 | 25/25 (100%) | 100% | 1.4s | $0.0021 | $0.83 | ✅ Production-ready |
| GLM 5.3 | 25/25 (100%) | 100% | 0.6s | $0.0036 | $1.44 | ✅ Production-ready |
| Gemini 3.8 Flash | 25/25 (100%) | 100% | 2.7s | $0.0286 | $11.44 | ✅ Production-ready |
| DeepSeek V4 Flash | 25/25 (100%) | 100% | 0.8s | $0.0016 | $0.65 | ✅ Production-ready |
| Qwen 3.8 Max (hosted) | 25/25 (100%) | 100% | 4.3s | $0.0324 | $12.96 | ✅ Production-ready |
| Kimi K3 | 25/25 (100%) | 100% | 1.9s | $0.0640 | $25.58 | ✅ Production-ready |
| Qwen 3.8 27B (local) | 25/25 (100%) | 100% | 9.1s | Free (local) | Free (local) | ✅ Production-ready |
| Claude Sonnet 5.5 | 24/25 (96%) | 98% | 2.8s | $0.0381 | $15.26 | ✅ Production-ready |

## Who served each answer

OpenRouter can send the same model ID to different hosts. If one model shows several hosts, treat its score as a mix until you pin a host.

- **Claude Haiku 5.5**: Claude Platform on AWS (25) · reasoning tokens: 856
- **GLM 5.3**: Wafer (25) · reasoning tokens: 74
- **Gemini 3.8 Flash**: Google (25) · reasoning tokens: 5552
- **DeepSeek V4 Flash**: CoreWeave (25) · reasoning tokens: 1996
- **Qwen 3.8 Max (hosted)**: Alibaba (25) · reasoning tokens: 1552
- **Kimi K3**: DeepInfra (25) · reasoning tokens: 1744
- **Qwen 3.8 27B (local)**: LM Studio (25) · reasoning tokens: 3409
- **Claude Sonnet 5.5**: Claude Platform on AWS (25) · reasoning tokens: 366

## Where each model slipped

**Claude Haiku 5.5**: no misses 🎯

**GLM 5.3**: no misses 🎯

**Gemini 3.8 Flash**: no misses 🎯

**DeepSeek V4 Flash**: no misses 🎯

**Qwen 3.8 Max (hosted)**: no misses 🎯

**Kimi K3**: no misses 🎯

**Qwen 3.8 27B (local)**: no misses 🎯

**Claude Sonnet 5.5**: 1 misses
- Sales Operations Manager → seniority: got "Manager", wanted "IC"

## How to read this
- **Got it fully right**: both department and seniority matched the answer key.
- **Partial credit**: half a point for each field. Useful for spotting "close but not quite."
- **Verdict** is based on partial credit. Local speed depends on your Mac, not the model alone.
- **Cost** is what OpenRouter reported for these calls. It does not include the 5.5% fee charged when you buy credits.
- **Reasoning tokens** are hidden thinking. They raise cost and time even when the visible answer is one line of JSON.
