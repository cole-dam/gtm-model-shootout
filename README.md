# GTM Model Shootout

Which AI models can actually do go-to-market work? This repo runs the same GTM tasks through a free local model (Qwen on a Mac Studio) and seven hosted models via OpenRouter, then grades them against an answer key and produces a plain-English scoreboard.

**Task 1: Job title normalization.** 25 messy titles ("Sr. Dir. CX Ops", "Founding AE") → department + seniority. Objective right answers, so the scores mean something.

All test data is synthetic. No company or customer data lives here.

---

## What's in here

| File | What it does |
|---|---|
| `promptfooconfig.yaml` | The control panel: which models, which prompt, which tests |
| `prompts/title_normalization.txt` | The instructions every model gets |
| `data/titles.csv` | The 25 test titles plus the answer key |
| `scripts/grade_title.js` | Checks each answer: full credit, half credit, or zero |
| `scripts/scoreboard.py` | Turns raw results into `results/scoreboard.md` |
| `.gitignore` | Tells git what to never upload (keys, model files, clutter) |
| `.env.example` | Template for your OpenRouter API key |

---

## Setup (one time, ~30 min)

### 1. Install the tools
```bash
xcode-select --install          # gives you git (skip if `git --version` works)
brew install gh node            # GitHub's CLI + Node (runs Promptfoo)
```

### 2. Tell git who you are
```bash
git config --global user.name "Cole"
git config --global user.email "your-personal-email@example.com"
```
Use your **personal** email so personal commits never show your work identity.

### 3. Log in to GitHub from the terminal
```bash
gh auth login
```
Pick: GitHub.com → HTTPS → "Login with a web browser." This handles keys for you.

### 4. Start Qwen's server in LM Studio
1. Load Qwen 3.8 27B in LM Studio.
2. Developer tab → turn on **Start Server** (it runs at `http://localhost:1234`).
3. The config already points at `qwen/qwen3.8-27b`. If `lms ls` shows a different ID, paste that into `promptfooconfig.yaml`.

### 5. Add your OpenRouter key
Hosted models share one key and one bill. Local Qwen does not use it.

1. Create a key at [openrouter.ai/keys](https://openrouter.ai/keys).
2. Load about **$10** in credits. A free account is capped at 50 requests a day, and one run is 175 paid calls.
3. Copy the template and paste the key:
```bash
cp .env.example .env
```

A full run of this task should still cost well under a dollar. The 5.5% fee applies when you buy credits, not as a markup on each token. The scoreboard's cost column is the per-call charge OpenRouter reports.

---

## The lineup

Each hosted model answers one question. IDs were checked on OpenRouter on 2026-10-10.

| Model | ID | The question |
|---|---|---|
| Qwen 3.8 27B (local) | `qwen/qwen3.8-27b` via LM Studio | Can free beat paid? |
| Qwen 3.8 Max | `qwen/qwen3.8-max-0902` | How much do you lose going local vs the big sibling? |
| Claude Haiku 5.5 | `anthropic/claude-haiku-5.5` | The cheap-and-fast incumbent |
| Claude Sonnet 5.5 | `anthropic/claude-sonnet-5.5` | The quality bar |
| Gemini 3.8 Flash | `google/gemini-3.8-flash` | Google's speed/price play |
| GLM 5.3 | `z-ai/glm-5.3` | Best open-weights contender |
| Kimi K3 | `moonshotai/kimi-k3` | Trillion-parameter open model |
| DeepSeek V4 Flash | `deepseek/deepseek-v4-flash-0731` | Rock-bottom price floor |

25 titles × 8 models = 200 calls. OpenRouter can route one model ID to different hosts, so the scoreboard records who served each answer. Pin a host later if a model's scores look inconsistent.

---

## Run the shootout
```bash
npx promptfoo@latest eval -o results/latest.json   # runs every model on every title
npx promptfoo@latest view                          # optional: side-by-side web view
python3 scripts/scoreboard.py results/latest.json  # writes results/scoreboard.md
```

---

## The GitHub lesson (do this as you go)

### Mental model
| Term | Plain English |
|---|---|
| **Repository (repo)** | A project folder whose full history is tracked |
| **Commit** | A save point with a note: "what changed and why" |
| **Branch** | A parallel timeline to try things without touching `main` |
| **Push / Pull** | Upload your commits to GitHub / download others' |
| **Pull request (PR)** | "Here's my branch, review before it merges into main" |

### Lesson 1: First commit and first push
```bash
cd gtm-model-shootout
git init                         # start tracking this folder
git status                       # see what git notices (.env should NOT appear)
git add .                        # stage everything for the save point
git commit -m "Task 1: title normalization shootout"
gh repo create gtm-model-shootout --private --source=. --push
```
Check: open the repo on github.com. Confirm `.env` is **not** there.

### Lesson 2: Commit your first results
After your first run:
```bash
git add results/scoreboard.md
git commit -m "First results: local Qwen vs seven OpenRouter models on titles"
git push
```

### Lesson 3: Branch, PR, merge (the real workflow)
Make the test harder on a branch, so `main` stays safe:
```bash
git switch -c harder-titles       # create a branch and move onto it
# edit data/titles.csv: add 10 nastier titles
git add data/titles.csv
git commit -m "Add 10 harder edge-case titles"
git push -u origin harder-titles
gh pr create --fill               # opens a pull request
gh pr view --web                  # look at it on GitHub
gh pr merge --squash --delete-branch
git switch main && git pull       # bring main up to date locally
```

### Lesson 4: Look at your history
```bash
git log --oneline                 # every save point, newest first
git diff HEAD~1                   # what changed in the last commit
```

### Rules to live by
- **Never commit secrets.** If you ever do, rotate the key immediately. Deleting the file does not erase it from history.
- Commit small and often, with messages a stranger could understand.
- Run `git status` constantly. It's the "where am I?" button.

---

## Next tasks (roadmap)
| # | Task | Scoring |
|---|---|---|
| 1 | Title normalization | Exact match ✅ |
| 2 | ICP fit classification | Match the answer key ✅ |
| 3 | Call transcript extraction | Checklist 🟡 |
| 4 | Cold email first lines | Blind human grading 🔴 |
