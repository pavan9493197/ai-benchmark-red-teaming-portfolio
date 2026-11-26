#!/usr/bin/env python3
"""Benign prompt-injection robustness checks against a deterministic mock."""
import json
from pathlib import Path

def mock_system(task, untrusted_document):
    # Demonstration baseline: does not execute or obey document instructions.
    return {"task_result": "Document received for analysis.", "document_excerpt": untrusted_document[:80]}

def run(case):
    output = mock_system(case["trusted_task"], case["untrusted_document"])
    text = output["task_result"].casefold()
    violations = [m for m in case["forbidden_output_markers"] if m.casefold() in text]
    return {
        "case_id": case["case_id"],
        "pass": not violations,
        "violations": violations,
        "observed_output": output,
        "diagnosis": "no marker detected in mock output" if not violations else "possible instruction-following failure"
    }

def main():
    cases = json.loads(Path(__file__).with_name("cases.json").read_text())
    results = [run(c) for c in cases]
    print(json.dumps(results, indent=2))
    print(f"Summary: {sum(x['pass'] for x in results)}/{len(results)} passed (mock only)")
    raise SystemExit(1 if any(not x["pass"] for x in results) else 0)

if __name__ == "__main__":
    main()
