#!/usr/bin/env python3
"""Validate research benchmark task metadata and evidence fields."""
import argparse
import json
from pathlib import Path
from urllib.parse import urlparse

REQUIRED = [
    "task_id", "question", "answer_key", "source_url",
    "supporting_excerpt", "retrieved_on", "ambiguity_notes"
]

def validate(task):
    missing = [key for key in REQUIRED if not str(task.get(key, "")).strip()]
    parsed = urlparse(task.get("source_url", ""))
    valid_url = parsed.scheme in ("http", "https") and bool(parsed.netloc)
    issues = []
    if missing:
        issues.append("Missing required fields: " + ", ".join(missing))
    if not valid_url:
        issues.append("source_url must be a complete http(s) URL")
    if len(task.get("supporting_excerpt", "")) < 20:
        issues.append("Supporting excerpt is very short; provide enough context to audit.")
    if task.get("source_type") not in ("primary", "secondary", "official_dataset", "other"):
        issues.append("source_type must be primary, secondary, official_dataset, or other")
    return {"task_id": task.get("task_id", "unknown"), "valid": not issues, "issues": issues}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    tasks = json.loads(Path(args.input).read_text())
    results = [validate(t) for t in tasks]
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(json.dumps(results, indent=2))
    print(f"Validated {len(results)} task(s); wrote {args.output}")
    raise SystemExit(1 if any(not x["valid"] for x in results) else 0)

if __name__ == "__main__":
    main()
