#!/usr/bin/env python3
"""Detect simple authentication patterns in synthetic JSONL events."""
import argparse, json
from collections import defaultdict
from pathlib import Path

def analyze(events, threshold=3):
    failures = defaultdict(list)
    findings = []
    for event in events:
        if event.get("event_type") == "login_failure":
            failures[(event.get("source_ip"), event.get("username"))].append(event)
    for (ip, user), rows in failures.items():
        if len(rows) >= threshold:
            findings.append({
                "rule_id": "AUTH-001",
                "severity": "medium",
                "source_ip": ip,
                "username": user,
                "failed_attempts": len(rows),
                "first_seen": min(r["timestamp"] for r in rows),
                "last_seen": max(r["timestamp"] for r in rows),
                "triage": "Review for password spraying/brute-force pattern; correlate with successful logins and asset context."
            })
    return findings

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True); ap.add_argument("--output", required=True)
    a = ap.parse_args()
    events = [json.loads(x) for x in Path(a.input).read_text().splitlines() if x.strip()]
    results = analyze(events)
    Path(a.output).parent.mkdir(parents=True, exist_ok=True)
    Path(a.output).write_text(json.dumps(results, indent=2))
    print(f"Processed {len(events)} events; {len(results)} finding(s). Output: {a.output}")

if __name__ == "__main__":
    main()
