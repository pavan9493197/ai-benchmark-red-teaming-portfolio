# AI Benchmark & Red-Teaming Portfolio

A small, reproducible portfolio demonstrating skills relevant to AI benchmark research:
- structured LLM response evaluation,
- prompt-injection robustness testing,
- evidence-backed web-research benchmark design,
- source traceability and failure analysis.

**Important:** These are independent portfolio projects using synthetic/example data. They are not work performed for CENIT Technologies, Turing, or another employer. Do not describe them as professional employment experience. Replace sample cases with your own independently researched and documented work before presenting them as completed research.

## Projects

### 1. LLM Response Evaluator
Location: `01_llm_response_evaluator/`

A Python CLI that compares a candidate answer against a reference answer using transparent rubric checks (exact-match tokens, required facts, unsupported-claim flags, and citation presence). It produces a JSON evaluation report. This is a lightweight demonstration, not a substitute for expert evaluation or semantic model judging.

Run:
```bash
python3 01_llm_response_evaluator/evaluate.py \
  --input data/sample_responses.jsonl \
  --output reports/evaluation_report.json
```

### 2. Prompt-Injection Red-Team Test Set
Location: `02_prompt_injection_redteam/`

A small test harness that checks whether a system under test follows a trusted task instruction when untrusted quoted content contains instruction-like text. The examples are benign and use a mock target by default. To evaluate a real model, implement `call_model()` yourself and follow that provider's terms and safety rules.

Run:
```bash
python3 02_prompt_injection_redteam/run_tests.py
```

### 3. Evidence-Backed Research Benchmark
Location: `03_research_benchmark/`

A benchmark-task template and validator for checking that each task includes a precise question, answer key, primary-source URL, supporting excerpt, retrieval date, and ambiguity notes. Sample task is illustrative; verify all facts and sources independently before using it as a real benchmark item.

Run:
```bash
python3 03_research_benchmark/validate_tasks.py \
  --input data/sample_benchmark_tasks.json \
  --output reports/benchmark_validation.json
```

## Suggested GitHub presentation

1. Create a public repository named `ai-benchmark-red-teaming-portfolio`.
2. Upload this folder's contents (not the ZIP file alone).
3. Run each command and commit the generated reports.
4. Add your own original benchmark items with source URLs and short evidence excerpts.
5. In your resume, label this as **Independent AI Evaluation & Red-Teaming Portfolio**.

## Skills demonstrated

Python, evaluation rubrics, test-case design, prompt-injection awareness, research-task specification, evidence traceability, JSON/JSONL processing, QA reporting, and root-cause categorization.

## Limitations

- The evaluator uses simple transparent heuristics, not a frontier-grade LLM judge.
- The red-team harness uses a mock target until you connect a model.
- The research validator checks completeness and URL format; it does not verify that a source is authoritative or that an answer is true.
- No hidden chain-of-thought is requested or stored. Evaluate observable outputs and tool/search logs only when lawfully available.
