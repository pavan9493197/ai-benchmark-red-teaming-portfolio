# G. Pavan | AI Benchmark & Red-Teaming Portfolio

This portfolio is tailored to the skills listed in my resume: LLM familiarity, AI response evaluation, prompt-injection awareness, AI security/risk assessment, Python, OSINT/reconnaissance tools, Splunk/SIEM log analysis, vulnerability assessment, CVE/CVSS risk prioritization, web application security testing, and technical documentation.

## Important scope and integrity note

These are **independent portfolio demonstrations**, built to show how I approach evaluation and analysis. They are not presented as code or deliverables produced for CENIT Technologies, Turing, or any other employer. The security logs, vulnerabilities, and model answers included here are synthetic examples. They do not establish that these exact scripts or datasets were used in my employment.

If a topic reflects work I actually performed professionally, I can describe that experience separately and accurately in an interview. This repository only contains the sample implementations included here.

## Projects

| Project | Resume skills reflected | Main demonstration |
|---|---|---|
| 01 LLM Evaluation | LLM familiarity, AI response evaluation, AI safety evaluation, technical documentation | Rubric-based factuality and citation checks |
| 02 Prompt-Injection Red Team | Prompt injection, LLM security, red-team awareness | Benign adversarial test cases and observable-output checks |
| 03 OSINT Research Benchmark | Maltego/theHarvester familiarity, reconnaissance, research | Evidence-backed task authoring and source traceability |
| 04 SIEM Log Analysis | Splunk, Sentinel, Wazuh, log analysis, threat hunting | Rule-based analysis of synthetic authentication events |
| 05 Vulnerability Risk Prioritization | Nmap, Nessus/OpenVAS, CVE/CVSS, remediation tracking | Transparent risk ranking and remediation queue |
| 06 Web App Security QA | Burp Suite, OWASP ZAP, SQL injection/XSS awareness | Structured finding review and QA checklist |

## Quick start

Requires Python 3.9+ and uses only the Python standard library.

```bash
python3 01_llm_evaluation/evaluate.py --input data/llm_cases.json --output reports/llm_evaluation.json
python3 02_prompt_injection_redteam/run_tests.py
python3 03_osint_research_benchmark/validate_benchmark.py --input data/research_tasks.json --output reports/research_validation.json
python3 04_siem_log_analysis/analyze_logs.py --input data/auth_events.jsonl --output reports/siem_findings.json
python3 05_vulnerability_risk_prioritization/prioritize.py --input data/vulnerabilities.json --output reports/vulnerability_queue.json
python3 06_web_app_security_qa/review_findings.py --input data/web_findings.json --output reports/web_qa_review.json
```

## How this maps to the Turing role

- **Benchmark task construction:** Project 03 uses a schema for clear questions, answer keys, evidence excerpts, and ambiguity notes.
- **Model evaluation:** Project 01 scores observable answers against explicit criteria. It is a transparent heuristic, not an expert replacement.
- **Red-teaming:** Project 02 tests whether instruction-like text inside untrusted content improperly changes the expected task behavior. It uses a mock target by default.
- **Failure diagnosis:** Projects 01 and 02 record specific observable failure categories. No hidden chain-of-thought is requested or claimed.
- **Research quality:** Project 03 checks evidence metadata and source traceability. Human verification is still required.
- **Transferable security analysis:** Projects 04–06 demonstrate structured log, vulnerability, and web finding review using synthetic data.

## Honest usage

Do not claim that the sample tasks have broken Claude, GPT, or another frontier model. Do not claim benchmark experience with GAIA, BrowseComp, SimpleQA, SWE-bench, Terminal-Bench, or HLE based only on these projects. These projects demonstrate foundational methods; they are not official benchmark implementations.

## Suggested next improvements

1. Add original research tasks after independently verifying each answer against primary sources.
2. Add a documented real-model adapter only if permitted by the provider and assessment rules.
3. Compare multiple model outputs and preserve prompts, outputs, timestamps, and source URLs.
4. Include manual reviewer notes and inter-rater agreement for a larger evaluation set.
