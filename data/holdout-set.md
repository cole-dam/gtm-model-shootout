# Holdout Set: Title Normalization

## What this is

All day we tuned the prompt by looking at misses on the 26 titles in `titles.csv`. That makes the prompt good at *those* titles, partly because we adjusted it around them. Think of them as practice problems with the answer key open.

This holdout set is the **real exam**: 25 brand-new titles the prompt was never adjusted for.

- 100% on practice + 100% on holdout = the instructions genuinely work.
- 100% on practice + 80% on holdout = we taught the models the answers.

**The one rule:** you can look at holdout results, but you can't change the prompt to fix holdout misses. If you do, this becomes practice problems too, and you need a fresh holdout set.

Fixing the prompt *before* the first holdout run is fine, since no model results have been seen yet.

## Status

**Approved 2026-10-10.** The answer key lives in `data/holdout.csv`. It runs from its own config and writes its own scoreboard, so it never overwrites the practice results.

```bash
npx promptfoo@latest eval -c promptfooconfig.holdout.yaml -o results/holdout.json
python3 scripts/scoreboard.py results/holdout.json results/holdout-scoreboard.md
```

## Design principles

- **New titles only.** Nothing from `titles.csv` or the prompt's examples.
- **One clear answer.** Would 9 out of 10 GTM leaders agree without being told? If not, cut it or add a rule.
- **Realistic.** Titles are written the way they actually appear on LinkedIn and in CRMs, including real-world noise like pipes, "@ Company," and hiring tags.

## Titles

| # | Title | Function | Seniority | What it tests |
|---|---|---|---|---|
| 1 | Senior Account Executive \| Mid-Market | Sales | IC | Noise: pipe suffix |
| 2 | Director of Field Marketing | Marketing | Director | Easy control |
| 3 | VP Sales (we're hiring!) | Sales | VP | Noise: hiring tag |
| 4 | SWE II | Engineering | IC | Abbreviation |
| 5 | Senior Accountant | Finance | IC | Easy control |
| 6 | Recruiter | People | IC | Easy control |
| 7 | Content Marketing Manager | Marketing | IC | Manager of a thing |
| 8 | Partner Marketing Manager | Marketing | IC | Manager of a thing |
| 9 | Product Marketing Manager | Marketing | IC | Manager of a thing |
| 10 | Senior Product Manager | Product | IC | Manager of a thing |
| 11 | Sales Operations Manager | Operations | IC | Manager of a function + Ops rule |
| 12 | Key Account Manager | Sales | IC | Account Manager rule |
| 13 | Senior Engineering Manager | Engineering | Manager | Manager of a team |
| 14 | AE Team Lead | Sales | Manager | Team Lead rule + abbreviation |
| 15 | Manager, Customer Success | Customer Success | Manager | "Manager," first = people manager |
| 16 | Head of RevOps @ Acme | Operations | Director | "Head of" rule + noise |
| 17 | VP, Head of Customer Success | Customer Success | VP | VP beats "Head of" |
| 18 | Chief Product Officer | Product | C-Level | Chief + department |
| 19 | Chief People Officer | People | C-Level | Chief + department |
| 20 | Founder & CTO | Executive | C-Level | Founder rule beats department |
| 21 | Customer Support Supervisor | Customer Support | Manager | Supervisor rule |
| 22 | Sales Development Team Lead | Sales | Manager | Team Lead rule |
| 23 | Marketing Operations Specialist | Operations | IC | Ops rule |
| 24 | Customer Onboarding Manager | Customer Success | IC | Onboarding + Manager trap |
| 25 | Director of Sales Operations | Operations | Director | Ops rule |

### Rules being tested (from the prompt)

| Rule | Plain English |
|---|---|
| "Head of" rule | "Head of X" is Director unless the title also says VP or Chief |
| Founder rule | Anyone with Founder or CEO in their title is Executive, C-Level, whatever their other title |
| Chief + department | Other C-level titles take the department they name (CMO → Marketing) |
| Ops rule | RevOps, Sales Ops, and Marketing Ops go in Operations, not the team they support |
| Team Lead / Supervisor rule | Both count as Manager |
| Manager rule | "Manager" of a team of people = Manager; "Manager" of a thing (account, channel, product, function) = IC |
| "Manager," first rule | "Manager, [team]" with Manager first = people manager |
| Account Manager rule | Account Managers = Sales; onboarding of existing customers = Customer Success |

## Decisions log (resolved 2026-10-10 before any holdout run)

These changed the prompt. That's allowed because no holdout results had been seen yet.

| Question | Decision | Prompt change |
|---|---|---|
| What does "Manager, Customer Success" mean? | Almost always a people manager (~2% IC) | Added the "Manager," first rule |
| Where do Key Account Managers sit? | Sales | Account Managers moved from Customer Success to Sales |
| Is Founder & CTO Engineering or Executive? | Same as Founder & CEO: Executive | Added the Founder rule |
| Product Marketing / Partner Marketing Manager? | Marketing IC | None |

Because the prompt changed, **rerun the practice set too** so practice and holdout scores come from the same frozen prompt.

## Known gaps in the prompt

- **Support Ops / CX Ops** isn't covered by the Ops rule. That's why "Sr. Dir. CX Ops" was cut from the practice set.

## Next steps

1. ~~Resolve open questions~~ ✅
2. ~~Create `data/holdout.csv` and `promptfooconfig.holdout.yaml`~~ ✅
3. Freeze the prompt. Rerun the practice set with it.
4. Run the holdout once. Compare practice vs holdout. Don't tune the prompt against holdout misses.
