"""Turn Promptfoo's raw results into a plain-English scoreboard.

Usage:  python3 scripts/scoreboard.py results/latest.json
Writes: results/scoreboard.md  (and prints it)
"""

import json
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path


def load_rows(path):
    data = json.loads(Path(path).read_text())
    # Promptfoo nests results differently across versions; handle both shapes.
    results = data.get("results", data)
    if isinstance(results, dict):
        results = results.get("results", [])
    return results, data


def verdict(accuracy):
    if accuracy >= 0.95:
        return "✅ Production-ready"
    if accuracy >= 0.85:
        return "🟡 Good with spot checks"
    if accuracy >= 0.70:
        return "🟠 Needs human review"
    return "🔴 Not trustworthy yet"


def _host_name(value):
    if isinstance(value, str) and value.strip():
        return value.strip()
    return None


def _cache_host_index():
    """Map each cached OpenRouter reply to the company that served it.

    The chat completion body includes `provider` (for example "Google Vertex").
    Promptfoo stores that body in its disk cache and copies only the bill into
    the eval output, so the exported results do not contain the host.
    """
    path = Path.home() / ".promptfoo" / "cache" / "cache.json"
    exact = {}
    by_output = {}
    if not path.exists():
        return exact, by_output
    try:
        entries = json.loads(path.read_text()).get("cache") or []
    except (OSError, json.JSONDecodeError):
        return exact, by_output
    for entry in entries:
        if not isinstance(entry, list) or len(entry) < 2:
            continue
        payload = entry[1]
        if not isinstance(payload, dict):
            continue
        try:
            outer = json.loads(payload.get("value") or "")
            inner = json.loads(outer.get("value") or "")
        except (TypeError, json.JSONDecodeError):
            continue
        body = inner.get("data") if isinstance(inner, dict) else None
        if not isinstance(body, dict):
            continue
        host = _host_name(body.get("provider"))
        model = body.get("model")
        choices = body.get("choices") or []
        message = choices[0].get("message") if choices and isinstance(choices[0], dict) else None
        content = (message or {}).get("content") if isinstance(message, dict) else None
        usage = body.get("usage") if isinstance(body.get("usage"), dict) else {}
        if not host or not isinstance(model, str) or not isinstance(content, str):
            continue
        exact.setdefault(
            (model, content, usage.get("prompt_tokens"), usage.get("completion_tokens")),
            set(),
        ).add(host)
        by_output.setdefault((model, content), set()).add(host)
    return exact, by_output


def serving_host(row, cache_index=None):
    """Name of the company that actually answered.

    OpenRouter can route one model ID to different companies. Promptfoo keeps
    the raw body in its cache; `provider` on that body is the serving host.
    """
    response = row.get("response") or {}
    meta = response.get("metadata") or {}
    row_meta = row.get("metadata") if isinstance(row.get("metadata"), dict) else {}
    openrouter = meta.get("openrouter") if isinstance(meta, dict) else None
    raw = response.get("raw")
    candidates = []
    if isinstance(openrouter, dict):
        candidates.extend([openrouter.get("provider"), openrouter.get("providerName")])
    if isinstance(meta, dict):
        candidates.append(meta.get("provider"))
    if isinstance(row_meta, dict):
        nested = row_meta.get("openrouter")
        if isinstance(nested, dict):
            candidates.extend([nested.get("provider"), nested.get("providerName")])
    if isinstance(raw, dict):
        candidates.append(raw.get("provider"))
        nested = raw.get("response")
        if isinstance(nested, dict):
            candidates.append(nested.get("provider"))
    for candidate in candidates:
        name = _host_name(candidate)
        if name:
            return name

    provider = row.get("provider") or {}
    provider_id = provider.get("id") or ""
    if isinstance(provider_id, str) and provider_id.startswith("openrouter:"):
        model = provider_id.split(":", 1)[1]
        output = response.get("output")
        if not isinstance(output, str):
            output = "" if output is None else str(output)
        usage = row.get("tokenUsage") or response.get("tokenUsage") or {}
        if not isinstance(usage, dict):
            usage = {}
        exact, by_output = cache_index if cache_index is not None else _cache_host_index()
        hosts = exact.get((model, output, usage.get("prompt"), usage.get("completion")))
        if not hosts:
            hosts = by_output.get((model, output))
        if hosts and len(hosts) == 1:
            return next(iter(hosts))

    label = provider.get("label") or ""
    if isinstance(label, str) and "local" in label.lower():
        return "LM Studio"
    return None


def reasoning_tokens(row):
    response = row.get("response") or {}
    usage = row.get("tokenUsage") or response.get("tokenUsage") or {}
    if not isinstance(usage, dict):
        return 0
    details = usage.get("completionDetails") or usage.get("completion_tokens_details") or {}
    if isinstance(details, dict):
        value = details.get("reasoning") or details.get("reasoning_tokens") or 0
        try:
            return int(value)
        except (TypeError, ValueError):
            return 0
    return 0


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "results/latest.json"
    rows, raw = load_rows(path)
    if not rows:
        sys.exit(f"No results found in {path}. Did the eval run?")

    stats = defaultdict(lambda: {
        "n": 0,
        "pass": 0,
        "score": 0.0,
        "latency": [],
        "cost": 0.0,
        "reasoning": 0,
        "hosts": defaultdict(int),
        "misses": [],
    })
    cache_index = _cache_host_index()
    for r in rows:
        provider = r.get("provider") or {}
        name = provider.get("label") or provider.get("id") or "unknown"
        s = stats[name]
        s["n"] += 1
        s["pass"] += 1 if r.get("success") else 0
        s["score"] += float(r.get("score") or 0)
        if r.get("latencyMs") is not None:
            s["latency"].append(r["latencyMs"])
        s["cost"] += float(r.get("cost") or 0)
        s["reasoning"] += reasoning_tokens(r)
        host = serving_host(r, cache_index)
        if host:
            s["hosts"][host] += 1
        if not r.get("success"):
            title = (r.get("vars") or {}).get("title", "?")
            reason = (r.get("gradingResult") or {}).get("reason", "")
            s["misses"].append(f"{title} → {reason}")

    lines = [
        f"# GTM Model Shootout: Title Normalization",
        f"_Run on {date.today().isoformat()} · {next(iter(stats.values()))['n']} job titles_",
        "",
        "| Model | Got it fully right | Partial credit score | Avg speed | Cost for this run | Cost per 10k titles | Verdict |",
        "|---|---|---|---|---|---|---|",
    ]
    ranked = sorted(stats.items(), key=lambda kv: kv[1]["score"] / kv[1]["n"], reverse=True)
    for name, s in ranked:
        acc = s["pass"] / s["n"]
        partial = s["score"] / s["n"]
        avg_s = (sum(s["latency"]) / len(s["latency"]) / 1000) if s["latency"] else 0
        is_local = "local" in name.lower()
        cost = "Free (local)" if is_local else (f"${s['cost']:.4f}" if s["cost"] else "n/a")
        per10k = "Free (local)" if is_local else (f"${s['cost'] / s['n'] * 10000:.2f}" if s["cost"] else "n/a")
        lines.append(
            f"| {name} | {s['pass']}/{s['n']} ({acc:.0%}) | {partial:.0%} | {avg_s:.1f}s | {cost} | {per10k} | {verdict(partial)} |"
        )

    lines += ["", "## Who served each answer", ""]
    lines.append("OpenRouter can send the same model ID to different hosts. If one model shows several hosts, treat its score as a mix until you pin a host.")
    lines.append("")
    for name, s in ranked:
        if not s["hosts"]:
            host_text = "not recorded"
        else:
            host_text = ", ".join(f"{host} ({count})" for host, count in sorted(s["hosts"].items()))
        reasoning = f" · reasoning tokens: {s['reasoning']}" if s["reasoning"] else ""
        lines.append(f"- **{name}**: {host_text}{reasoning}")

    lines += ["", "## Where each model slipped", ""]
    for name, s in ranked:
        lines.append(f"**{name}**: " + (f"{len(s['misses'])} misses" if s["misses"] else "no misses 🎯"))
        for m in s["misses"]:
            lines.append(f"- {m}")
        lines.append("")

    lines += [
        "## How to read this",
        "- **Got it fully right**: both department and seniority matched the answer key.",
        "- **Partial credit**: half a point for each field. Useful for spotting \"close but not quite.\"",
        "- **Verdict** is based on partial credit. Local speed depends on your Mac, not the model alone.",
        "- **Cost** is what OpenRouter reported for these calls. It does not include the 5.5% fee charged when you buy credits.",
        "- **Reasoning tokens** are hidden thinking. They raise cost and time even when the visible answer is one line of JSON.",
    ]

    out = "\n".join(lines)
    Path("results").mkdir(exist_ok=True)
    Path("results/scoreboard.md").write_text(out + "\n")
    print(out)


if __name__ == "__main__":
    main()
