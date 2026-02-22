# M4U2 — NLP for Construction Document Analysis

## Assignment Overview

**Module:** M4 Unit 2 — Natural Language Processing  
**Programme:** Master's in AI for Architecture & Construction (Zigurat)

This assignment applies **NLP techniques** to a real construction contract, demonstrating how unstructured legal text can be converted into structured, machine-readable data. It covers information extraction, AI-assisted summarisation, prompt engineering, and critical reflection on AI limitations in a professional construction context.

---

## Files

| File                                 | Description                                                                            |
| ------------------------------------ | -------------------------------------------------------------------------------------- |
| `M4_U2_Assignment_Task.md`           | Assignment brief and rubric                                                            |
| `M4_U2_Assignment_Provided_case.pdf` | Source document (construction contract excerpt)                                        |
| `m4_u2_nlp_assignment_02.py`         | Full NLP pipeline — extracts data, generates summary, documents prompts, writes report |
| `structured_extraction.json`         | Part 1 output — structured JSON extraction of the contract                             |
| `M4_U2_Assignment_Report.md`         | Full report (Markdown source)                                                          |
| `M4_U2_Assignment_Report.pdf`        | **Final deliverable (PDF)**                                                            |

---

## Assignment Parts

| Part | Task                                           | Status                       |
| ---- | ---------------------------------------------- | ---------------------------- |
| 1    | Information Extraction → structured JSON       | ✅                           |
| 2    | Document Summary (< 200 words)                 | ✅ 164 words                 |
| 3    | Prompt Engineering Documentation (≥ 3 prompts) | ✅ 4 prompts with refinement |
| 4    | Critical Commentary (250–300 words)            | ✅ 290 words                 |

---

## NLP Pipeline

The `m4_u2_nlp_assignment_02.py` script implements a rule-based NLP pipeline using Python's `re` module:

- **Date extraction** — multi-pattern regex for ordinal and numeric dates
- **Monetary value extraction** — GBP currency pattern matching
- **Party extraction** — named entity patterns with role labels (Client / Contractor)
- **Obligation extraction** — modal verb detection (`shall`, `must`, `is responsible for`)
- **Risk/penalty extraction** — keyword-based sentence filtering
- **Location & project type** — contextual phrase matching
- **Governing law & dispute resolution** — targeted clause extraction

Running the script regenerates both `structured_extraction.json` and `M4_U2_Assignment_Report.md`.

---

## Running the Script

```bash
python3 m4_u2_nlp_assignment_02.py
```

No external dependencies required — uses Python standard library only (`re`, `json`).

---

_M4U2 Assignment — MAICEN-1125 | Zigurat Institute of Technology_
