#!/usr/bin/env python3
"""Check research benchmark task clarity and evidence metadata."""
import argparse, json
from pathlib import Path
from urllib.parse import urlparse

FIELDS = ["task_id", "question", "answer_key", "source_url", "supporting_excerpt",
          "retrieved_on", "source_type", "ambiguity_notes"]

def validate(task):
    issues = [f"missing:{k}" for k in FIELDS if not str(task.get(k, "")).strip()]
    u = urlparse(task.get("source_url", ""))
    if u.scheme not in ("http", "https") or not u.netloc:
        issues.append("source_url_not_valid_http(s)")
    if len(task.get("question", "")) < 25:
        issues.append("question_may_be_under-specified")
    if len(task.get("supporting_excerpt", "")) < 30:
        issues.append("supporting_excerpt_too_short_for_audit")
    if task.get("source_type") not in {"primary", "official_dataset", "secondary"}:
        issues.append("source_type_must_be_classified")
    if task.get("answer_key") in {"TODO", "VERIFY_BEFORE_USE"}:
        issues.append("answer_key_not_verified")
    return {"task_id": task.get("task_id", "unknown"), "valid_metadata": not issues, "issues": issues,
            "human_fact_check_required": True}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True); ap.add_argument("--output", required=True)
    a = ap.parse_args()
    tasks = json.loads(Path(a.input).read_text())
    result = [validate(t) for t in tasks]
    Path(a.output).parent.mkdir(parents=True, exist_ok=True)
    Path(a.output).write_text(json.dumps(result, indent=2))
    print(f"Reviewed {len(result)} task record(s): {a.output}")
    raise SystemExit(1 if any(not x["valid_metadata"] for x in result) else 0)

if __name__ == "__main__":
    main()
