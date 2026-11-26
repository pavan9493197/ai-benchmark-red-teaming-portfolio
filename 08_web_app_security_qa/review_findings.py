#!/usr/bin/env python3
"""QA-check completeness of web application security findings."""
import argparse, json
from pathlib import Path

REQUIRED = ["finding_id", "title", "affected_component", "evidence", "severity",
            "impact", "remediation", "retest_status"]

def review(f):
    missing = [k for k in REQUIRED if not str(f.get(k, "")).strip()]
    valid_severity = f.get("severity") in {"Critical", "High", "Medium", "Low", "Informational"}
    if not valid_severity: missing.append("severity_must_use_defined_scale")
    return {"finding_id": f.get("finding_id", "unknown"),
            "documentation_complete": not missing,
            "missing_or_invalid": missing,
            "reviewer_note": "Confirm evidence is reproducible and remediation is retested."}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True); ap.add_argument("--output", required=True)
    a = ap.parse_args()
    data = json.loads(Path(a.input).read_text())
    results = [review(x) for x in data]
    Path(a.output).parent.mkdir(parents=True, exist_ok=True)
    Path(a.output).write_text(json.dumps(results, indent=2))
    print(f"QA-reviewed {len(results)} finding(s): {a.output}")

if __name__ == "__main__":
    main()
