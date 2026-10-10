# GTM Model Shootout: Title Normalization
_Run on 2026-10-10 · 25 job titles_

| Model | Got it fully right | Partial credit score | Avg speed | Cost for this run | Cost per 10k titles | Verdict |
|---|---|---|---|---|---|---|
| Claude Sonnet 5.5 | 24/25 (96%) | 98% | 2.1s | $0.0328 | $13.12 | ✅ Production-ready |
| GLM 5.3 | 24/25 (96%) | 98% | 3.1s | $0.0165 | $6.60 | ✅ Production-ready |
| Gemini 3.8 Flash | 24/25 (96%) | 98% | 3.1s | $0.0320 | $12.79 | ✅ Production-ready |
| Kimi K3 | 24/25 (96%) | 98% | 2.2s | $0.0553 | $22.13 | ✅ Production-ready |
| Qwen 3.8 Max (hosted) | 23/25 (92%) | 96% | 7.2s | $0.0445 | $17.79 | ✅ Production-ready |
| DeepSeek V4 Flash | 23/25 (92%) | 96% | 2.2s | $0.0017 | $0.69 | ✅ Production-ready |
| Qwen 3.8 27B (local) | 22/25 (88%) | 94% | 8.1s | Free (local) | Free (local) | 🟡 Good with spot checks |
| Claude Haiku 5.5 | 22/25 (88%) | 94% | 1.5s | $0.0020 | $0.80 | 🟡 Good with spot checks |

## Who served each answer

OpenRouter can send the same model ID to different hosts. If one model shows several hosts, treat its score as a mix until you pin a host.

- **Claude Sonnet 5.5**: Claude Platform on AWS (25) · reasoning tokens: 695
- **GLM 5.3**: AkashML (1), Baidu (3), Decart (3), DigitalOcean (1), InferenceNet (1), Mistral (7), Parasail (1), PrimeIntellect (1), Sail Research (5), Wafer (2) · reasoning tokens: 3104
- **Gemini 3.8 Flash**: Google (25) · reasoning tokens: 6941
- **Kimi K3**: Decart (1), DigitalOcean (2), Fireworks (2), InferenceNet (5), Makora (5), Modal (4), Parasail (2), Relace (1), Wafer (3) · reasoning tokens: 2213
- **Qwen 3.8 Max (hosted)**: Alibaba (25) · reasoning tokens: 4358
- **DeepSeek V4 Flash**: Cohere (5), CoreWeave (7), DigitalOcean (5), OpenInference (4), Phala (1), Reka (1), StreamLake (1), Wafer (1) · reasoning tokens: 2446
- **Qwen 3.8 27B (local)**: LM Studio (25) · reasoning tokens: 3115
- **Claude Haiku 5.5**: Claude Platform on AWS (25) · reasoning tokens: 1400

## Where each model slipped

**Claude Sonnet 5.5**: 1 misses
- Lifecycle Marketing Manager → seniority: got "IC", wanted "Manager"

**GLM 5.3**: 1 misses
- Lifecycle Marketing Manager → seniority: got "IC", wanted "Manager"

**Gemini 3.8 Flash**: 1 misses
- Lifecycle Marketing Manager → seniority: got "IC", wanted "Manager"

**Kimi K3**: 1 misses
- Lifecycle Marketing Manager → seniority: got "IC", wanted "Manager"

**Qwen 3.8 Max (hosted)**: 2 misses
- Controller → seniority: got "Manager", wanted "Director"
- Group Product Manager → seniority: got "IC", wanted "Manager"

**DeepSeek V4 Flash**: 2 misses
- Lifecycle Marketing Manager → seniority: got "IC", wanted "Manager"
- Group Product Manager → seniority: got "IC", wanted "Manager"

**Qwen 3.8 27B (local)**: 3 misses
- Customer Success Manager → seniority: got "Manager", wanted "IC"
- Controller → seniority: got "IC", wanted "Director"
- Group Product Manager → seniority: got "IC", wanted "Manager"

**Claude Haiku 5.5**: 3 misses
- RevOps Manager → seniority: got "IC", wanted "Manager"
- Lifecycle Marketing Manager → seniority: got "IC", wanted "Manager"
- Controller → seniority: got "Manager", wanted "Director"

## How to read this
- **Got it fully right**: both department and seniority matched the answer key.
- **Partial credit**: half a point for each field. Useful for spotting "close but not quite."
- **Verdict** is based on partial credit. Local speed depends on your Mac, not the model alone.
- **Cost** is what OpenRouter reported for these calls. It does not include the 5.5% fee charged when you buy credits.
- **Reasoning tokens** are hidden thinking. They raise cost and time even when the visible answer is one line of JSON.
