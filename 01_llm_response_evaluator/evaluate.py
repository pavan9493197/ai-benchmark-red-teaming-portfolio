#!/usr/bin/env python3
"""Evaluate answer records against a small, explicit rubric."""
import argparse
import json
import re
from pathlib import Path

def tokens(text):
    return set(re.findall(r"[a-z0-9]+", text.lower()))

def evaluate(record):
    answer = str(record.get("candidate_answer") or "")
    reference = str(record.get("reference_answer") or "")
    required = record.get("required_facts") or []
    citations = record.get("citations") or []
    unsupported_markers = record.get("known_unsupported_claims") or []

    answer_tokens = tokens(answer)
    ref_tokens = tokens(reference)
    overlap = len(answer_tokens & ref_tokens) / max(1, len(ref_tokens))
    fact_results = [
        {"fact": str(fact), "present": str(fact).lower() in answer.lower()}
        for fact in required
    ]
    unsupported_found = [
        str(phrase) for phrase in unsupported_markers
        if str(phrase).lower() in answer.lower()
    ]

    scores = {
        "reference_token_overlap": round(overlap, 3),
        "required_fact_coverage": round(
            sum(x["present"] for x in fact_results) / max(1, len(fact_results)), 3
        ),
        "has_citation": bool(citations),
        "unsupported_marker_count": len(unsupported_found),
    }
    # Deliberately transparent weighted score; tune the rubric for each benchmark.
    total = (
        0.25 * scores["reference_token_overlap"]
        + 0.50 * scores["required_fact_coverage"]
        + 0.15 * int(scores["has_citation"])
        + 0.10 * int(not unsupported_found)
    )
    return {
        "task_id": record.get("task_id", "unknown"),
        "scores": scores,
        "required_facts": fact_results,
        "unsupported_markers_found": unsupported_found,
        "weighted_score": round(total, 3),
        "review_note": "Heuristic screening only; human review is required."
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    records = [json.loads(line) for line in Path(args.input).read_text().splitlines() if line.strip()]
    results = [evaluate(r) for r in records]
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(json.dumps(results, indent=2))
    print(f"Evaluated {len(results)} record(s); wrote {args.output}")

if __name__ == "__main__":
    main()
