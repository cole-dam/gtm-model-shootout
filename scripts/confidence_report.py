"""Does Jev know when it's wrong? Compares Jev's confidence on right vs wrong answers.

Usage:  python3 scripts/confidence_report.py results/latest.json results/jev-confidence.md
"""

import json
import sys
from pathlib import Path


def rows_from(path):
    data = json.loads(Path(path).read_text())
    results = data.get("results", data)
    return results.get("results", []) if isinstance(results, dict) else results


def main():
    src = sys.argv[1] if len(sys.argv) > 1 else "results/latest.json"
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("results/jev-confidence.md")

    by_model = {}
    for r in rows_from(src):
        label = (r.get("provider") or {}).get("label", "")
        if not label.startswith("Jev"):
            continue
        meta = (r.get("response") or {}).get("metadata") or {}
        fc, sc = meta.get("functionConfidence"), meta.get("seniorityConfidence")
        if fc is None or sc is None:
            continue
        by_model.setdefault(label, []).append({
            "title": (r.get("vars") or {}).get("title", "?"),
            "ok": bool(r.get("success")),
            "conf": min(fc, sc),  # an answer is only as sure as its least-sure half
            "fc": fc, "sc": sc,
            "reason": (r.get("gradingResult") or {}).get("reason", ""),
        })

    if not by_model:
        sys.exit(f"No Jev results with confidence found in {src}.")

    lines = ["# Does Jev know when it's wrong?", "",
             "Each answer's confidence is the lower of its department and seniority confidence.", ""]
    for label, rows in by_model.items():
        right = [x["conf"] for x in rows if x["ok"]]
        wrong = [x["conf"] for x in rows if not x["ok"]]
        avg = lambda xs: f"{sum(xs) / len(xs):.2f}" if xs else "n/a"
        lines += [f"## {label}", "",
                  f"- **Accuracy:** {len(right)}/{len(rows)}",
                  f"- **Average confidence when right:** {avg(right)}",
                  f"- **Average confidence when wrong:** {avg(wrong)}", "",
                  "### If you auto-accepted answers above a confidence threshold",
                  "", "| Threshold | Auto-accepted | Accuracy of auto-accepted | Sent to a human |",
                  "|---|---|---|---|"]
        for t in (0.5, 0.7, 0.8, 0.9, 0.95):
            acc = [x for x in rows if x["conf"] >= t]
            ok = sum(x["ok"] for x in acc)
            pct = f"{ok}/{len(acc)} ({ok / len(acc):.0%})" if acc else "n/a"
            lines.append(f"| {t:.2f} | {len(acc)}/{len(rows)} | {pct} | {len(rows) - len(acc)} |")
        misses = sorted((x for x in rows if not x["ok"]), key=lambda x: -x["conf"])
        lines += ["", "### Misses, most confident first", ""]
        lines += [f"- {x['title']} (confidence {x['conf']:.2f}) → {x['reason']}" for x in misses] or ["- None 🎯"]
        lines.append("")

    lines += ["## How to read this",
              "- **Good sign:** confidence is clearly lower when Jev is wrong. Then you can auto-accept the sure answers and route the rest to a person.",
              "- **Bad sign:** a confident miss. That's an error your process would wave straight through."]
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
