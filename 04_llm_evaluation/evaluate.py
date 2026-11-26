#!/usr/bin/env python3
"""Evaluate observable LLM answers with a transparent, configurable rubric."""
import argparse, json
from pathlib import Path

def evaluate(case):
    answer = case.get("candidate_answer", "")
    required = case.get("required_facts", [])
    forbidden = case.get("unsupported_claims_to_flag", [])
    sources = case.get("source_urls", [])
    fact_checks = [{"fact": f, "present": f.casefold() in answer.casefold()} for f in required]
    flagged = [x for x in forbidden if x.casefold() in answer.casefold()]
    coverage = sum(x["present"] for x in fact_checks) / max(1, len(fact_checks))
    citation_present = len(sources) > 0 and any(s in answer for s in sources)
    return {
        "case_id": case["case_id"],
        "required_fact_checks": fact_checks,
        "required_fact_coverage": round(coverage, 3),
        "citation_present_in_answer": citation_present,
        "unsupported_claims_flagged": flagged,
        "review_status": "human_review_required",
        "failure_category": (
            "missing_required_facts" if coverage < 1 else
            "unsupported_claim_detected" if flagged else
            "citation_not_in_answer" if not citation_present else
            "no_heuristic_issue_detected"
        )
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    cases = json.loads(Path(args.input).read_text())
    results = [evaluate(c) for c in cases]
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(json.dumps(results, indent=2))
    print(f"Evaluated {len(results)} answer(s): {args.output}")

if __name__ == "__main__":
    main()
