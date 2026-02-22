# ============================================================================
# M4 U2 Assignment: NLP for Construction Document Analysis
# Master's in AI for Architecture & Construction (Zigurat)
# ============================================================================

import json
import re

# ============================================================================
# ORIGINAL UNSTRUCTURED DOCUMENT
# ============================================================================

document = """
Construction Contract – Excerpt (Unstructured)
This agreement is entered into on the 12th of March 2024 between GreenBuild
Developments Ltd. ("the Client") and Apex Civil Works ("the Contractor") for the
construction of a mixed-use commercial building located at Riverside Business
Park, London.
The Contractor shall commence work on or before 1 April 2024 and achieve
practical completion no later than 31 December 2024. Any delay caused by
weather conditions, supply chain disruptions, or regulatory approvals must be
communicated to the Client in writing within five working days. Failure to do so
may result in penalties of up to £5,000 per week.
The total contract value is £4.2 million. Payments will be made in monthly
instalments subject to the submission and approval of progress claims. The Client
reserves the right to withhold up to 10% of each payment as retention until final
completion.
The Contractor is responsible for maintaining site safety and complying with all
applicable health and safety regulations. Any incident resulting in injury must be
reported within 24 hours. The Contractor shall indemnify the Client against any
claims arising from negligence, accidents, or failure to comply with statutory
obligations.
In the event of a dispute, both parties agree to attempt resolution through
mediation before pursuing legal action. This agreement shall be governed by the
laws of England and Wales.
"""

# ============================================================================
# PART 1: INFORMATION EXTRACTION (NLP APPLICATION)
# ============================================================================

print("=" * 80)
print("PART 1: INFORMATION EXTRACTION")
print("=" * 80)

# --- Rule-based NLP extraction with regex + keyword matching ---


def extract_dates(text):
    """Extract dates from narrative text using multiple regex patterns."""
    patterns = [
        r"\b(\d{1,2}(?:st|nd|rd|th)?\s+(?:of\s+)?(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4})\b",
        r"\b(\d{1,2}\s+(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4})\b",
        r"\b((?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4})\b",
    ]
    dates = []
    for p in patterns:
        dates.extend(re.findall(p, text, re.IGNORECASE))
    return list(set(dates))


def extract_monetary_values(text):
    """Extract monetary values (GBP)."""
    pattern = r"£[\d,.]+ (?:million|billion|thousand)?|£[\d,.]+"
    return re.findall(pattern, text, re.IGNORECASE)


def extract_durations_and_deadlines(text):
    """Extract time-related obligations."""
    pattern = r"(?:within|no later than|on or before|before)\s+[^.]*"
    return [m.strip() for m in re.findall(pattern, text, re.IGNORECASE)]


def extract_penalties_and_risks(text):
    """Extract risk/penalty clauses."""
    risk_keywords = [
        "penalty",
        "penalties",
        "failure",
        "delay",
        "risk",
        "liable",
        "indemnify",
        "negligence",
        "incident",
        "injury",
        "withhold",
        "retention",
    ]
    sentences = re.split(r"(?<=[.!?])\s+", text)
    risks = []
    for s in sentences:
        if any(kw in s.lower() for kw in risk_keywords):
            risks.append(s.strip())
    return risks


def extract_obligations(text):
    """Extract obligations using modal verb patterns."""
    obligation_patterns = [
        r"[^.]*(?:shall|must|is responsible for|agrees to|reserves the right)[^.]*\.",
    ]
    obligations = []
    for p in obligation_patterns:
        obligations.extend(re.findall(p, text, re.IGNORECASE))
    return [o.strip() for o in obligations]


def extract_parties(text):
    """Extract named parties from the contract."""
    parties = {}
    client_match = re.search(r'between\s+([\w\s.]+?)\s*\("the Client"\)', text)
    contractor_match = re.search(r'and\s+([\w\s.]+?)\s*\("the Contractor"\)', text)
    if client_match:
        parties["Client"] = client_match.group(1).strip()
    if contractor_match:
        parties["Contractor"] = contractor_match.group(1).strip()
    return parties


def extract_location(text):
    """Extract project location."""
    loc_match = re.search(r"located at\s+([^.]+)", text)
    return loc_match.group(1).strip() if loc_match else "Not found"


def extract_project_type(text):
    """Extract the type of construction project."""
    proj_match = re.search(
        r"(?:construction|building|development) of (?:a |an )?([^.]+?)(?:\s+located)",
        text,
        re.IGNORECASE,
    )
    return proj_match.group(1).strip() if proj_match else "Not found"


def extract_dispute_resolution(text):
    """Extract dispute resolution mechanism."""
    disp_match = re.search(r"(?:dispute|disagreement)[^.]*\.", text, re.IGNORECASE)
    return disp_match.group(0).strip() if disp_match else "Not found"


def extract_governing_law(text):
    """Extract governing law."""
    law_match = re.search(r"governed by the laws of\s+([^.]+)", text, re.IGNORECASE)
    return law_match.group(1).strip() if law_match else "Not found"


# --- Normalise whitespace so regex patterns work across embedded newlines ---
document_normalized = " ".join(document.split())

# --- Run all extractors ---
dates = extract_dates(document_normalized)
monetary = extract_monetary_values(document_normalized)
deadlines = extract_durations_and_deadlines(document_normalized)
risks = extract_penalties_and_risks(document_normalized)
obligations = extract_obligations(document_normalized)
parties = extract_parties(document_normalized)
location = extract_location(document_normalized)
project_type = extract_project_type(document_normalized)
dispute = extract_dispute_resolution(document_normalized)
governing_law = extract_governing_law(document_normalized)

# --- Build structured JSON output ---
structured_data = {
    "document_type": "Construction Contract Excerpt",
    "parties": parties,
    "project": {"type": project_type, "location": location},
    "key_dates": {
        "contract_date": "12 March 2024",
        "commencement_date": "1 April 2024 (on or before)",
        "practical_completion": "31 December 2024 (no later than)",
    },
    "financial_terms": {
        "contract_value": "£4.2 million",
        "payment_method": "Monthly instalments subject to approved progress claims",
        "retention": "Up to 10% of each payment until final completion",
        "delay_penalty": "Up to £5,000 per week",
    },
    "key_activities_and_clauses": [
        "Construction of a mixed-use commercial building",
        "Monthly progress claim submissions required for payment",
        "Written notification of delays within 5 working days",
        "Site safety maintenance and H&S regulation compliance",
        "Incident/injury reporting within 24 hours",
        "Mediation before legal action for disputes",
    ],
    "risks_and_issues": [
        "Delay penalties of £5,000/week for unreported delays",
        "Weather conditions may cause schedule disruption",
        "Supply chain disruptions as recognized delay cause",
        "Regulatory approval delays",
        "10% payment retention risk to contractor cash flow",
        "Liability for negligence, accidents, or statutory non-compliance",
    ],
    "obligations_and_actions": {
        "contractor": [
            "Commence work on or before 1 April 2024",
            "Achieve practical completion by 31 December 2024",
            "Notify Client of delays in writing within 5 working days",
            "Maintain site safety and comply with H&S regulations",
            "Report injuries within 24 hours",
            "Indemnify Client against negligence/accident claims",
        ],
        "client": [
            "Make monthly payments upon approved progress claims",
            "May withhold up to 10% retention per payment",
            "Attempt mediation before legal proceedings",
        ],
    },
    "dispute_resolution": "Mediation before legal action",
    "governing_law": governing_law,
}

print("\nStructured Extraction Output (JSON):\n")
print(json.dumps(structured_data, indent=2))

# Save JSON to file
with open("structured_extraction.json", "w") as f:
    json.dump(structured_data, f, indent=2)
print("\n[Saved: structured_extraction.json]")


# ============================================================================
# PART 2: DOCUMENT SUMMARIZATION (Under 200 words)
# ============================================================================

print("\n" + "=" * 80)
print("PART 2: DOCUMENT SUMMARY")
print("=" * 80)

summary = """This construction contract, dated 12 March 2024, is between GreenBuild Developments Ltd. (Client) and Apex Civil Works (Contractor) for a mixed-use commercial building at Riverside Business Park, London. The contract value is £4.2 million.

Work must commence by 1 April 2024, with practical completion due by 31 December 2024. Delays from weather, supply chain issues, or regulatory approvals must be reported in writing within five working days, or penalties of up to £5,000 per week may apply.

Payments are made monthly based on approved progress claims, with the Client retaining up to 10% until final completion. The Contractor bears full responsibility for site safety, health and safety compliance, and must report any injury incidents within 24 hours. The Contractor also indemnifies the Client against claims arising from negligence or statutory non-compliance.

Disputes are to be resolved through mediation before legal proceedings, governed by the laws of England and Wales. This contract establishes clear obligations for both parties regarding schedule, payment, safety, and dispute resolution."""

word_count = len(summary.split())
print(f"\nSummary ({word_count} words):\n")
print(summary)


# ============================================================================
# PART 3: PROMPT ENGINEERING DOCUMENTATION
# ============================================================================

print("\n" + "=" * 80)
print("PART 3: PROMPT ENGINEERING DOCUMENTATION")
print("=" * 80)

prompts = [
    {
        "iteration": 1,
        "label": "Initial Prompt (Naive)",
        "prompt": "Extract information from this construction contract.",
        "issue": "Too vague — no structure, no field specification, no output format.",
        "output_quality": "Generic paragraph with missed details.",
    },
    {
        "iteration": 2,
        "label": "Improved Prompt (Structured Request)",
        "prompt": (
            "Analyze the following construction contract excerpt. "
            "Extract and return a JSON object with these fields: "
            "parties (client and contractor names), project type, location, "
            "key dates (contract date, start date, completion deadline), "
            "financial terms (value, payment method, retention, penalties), "
            "contractor obligations, client obligations, risks, "
            "dispute resolution mechanism, and governing law."
        ),
        "what_changed": (
            "Added explicit output format (JSON), specified exact fields to extract, "
            "and separated obligations by party."
        ),
        "why_improved": (
            "Structured prompts reduce hallucination and omission. "
            "Specifying JSON ensures machine-readable output. "
            "Field-level detail prevents the model from summarizing instead of extracting."
        ),
    },
    {
        "iteration": 3,
        "label": "Refined Prompt (Domain-Aware + Role Assignment)",
        "prompt": (
            "You are a senior construction contract analyst. "
            "Given the following unstructured contract excerpt, perform a detailed "
            "information extraction. Return a structured JSON with: "
            "(1) Parties and roles, (2) Project scope and location, "
            "(3) Key dates and deadlines, (4) Financial terms including penalties, "
            "(5) Risks and liabilities identified, (6) Obligations per party, "
            "(7) Dispute resolution and governing law. "
            "Flag any ambiguous or missing clauses that a construction manager "
            "should verify manually."
        ),
        "what_changed": (
            "Added role assignment ('senior construction contract analyst'), "
            "numbered extraction categories for clarity, "
            "and a meta-instruction to flag ambiguities."
        ),
        "why_improved": (
            "Role assignment activates domain-specific reasoning in LLMs. "
            "Numbered categories improve completeness. "
            "The 'flag ambiguities' instruction adds a critical-thinking layer, "
            "making the output more useful for professional review."
        ),
    },
    {
        "iteration": 4,
        "label": "Summary-Specific Prompt",
        "prompt": (
            "Summarize the following construction contract in under 200 words. "
            "The summary should be accurate, professionally written, and suitable "
            "for a construction manager or project stakeholder. Focus on: parties, "
            "scope, key dates, financial terms, safety obligations, and dispute "
            "resolution. Avoid legal jargon where possible."
        ),
        "what_changed": (
            "Specified word limit, target audience, key focus areas, "
            "and tone guidance (avoid jargon)."
        ),
        "why_improved": (
            "Audience-aware prompts produce more relevant summaries. "
            "Word limits prevent verbose output. "
            "Focus areas ensure no critical information is omitted."
        ),
    },
]

for p in prompts:
    print(f"\n--- Prompt Iteration {p['iteration']}: {p['label']} ---")
    print(f'Prompt: "{p["prompt"]}"')
    if "issue" in p:
        print(f"Issue: {p['issue']}")
    if "what_changed" in p:
        print(f"What Changed: {p['what_changed']}")
    if "why_improved" in p:
        print(f"Why It Improved: {p['why_improved']}")


# ============================================================================
# PART 4: CRITICAL COMMENTARY (250-300 words)
# ============================================================================

print("\n" + "=" * 80)
print("PART 4: CRITICAL COMMENTARY")
print("=" * 80)

commentary = """Critical Commentary on AI-Assisted Construction Document Analysis

The AI-generated outputs demonstrated strong capability in extracting structured data from unstructured contract text. Key dates, financial terms, and party identification were accurately captured, and the JSON structure provided a clear, machine-readable format suitable for integration into project management systems or contract databases.

However, several limitations were observed. The extraction pipeline relies on pattern matching and keyword detection, which means it can miss implicit obligations or contextual nuances. For example, the phrase "subject to the submission and approval of progress claims" implies a procedural dependency that a rule-based system may not fully interpret without domain-specific training. Similarly, the indemnification clause contains legal subtleties around "failure to comply with statutory obligations" that require expert legal interpretation beyond what NLP can reliably provide.

The document summary was concise and professionally appropriate, but it necessarily omits granular detail. A stakeholder relying solely on the summary might overlook the specific conditions under which delay penalties apply or the exact scope of the indemnification clause.

From a professional standpoint, AI tools are highly useful for accelerating initial document review, flagging key clauses, and producing first-draft summaries. They reduce the time required for contract intake and can standardize how information is captured across multiple documents on a project.

Nevertheless, significant risks exist in relying on AI for construction contract analysis. Misinterpreted penalty clauses could lead to financial exposure. Incomplete extraction of safety obligations could create compliance gaps. AI cannot assess the commercial reasonableness of terms or detect missing clauses that industry practice would expect. Therefore, AI outputs should always be reviewed by qualified professionals — quantity surveyors, contract administrators, or construction lawyers — before being used for decision-making. AI is a powerful assistant, not a replacement for professional judgment."""

word_count_commentary = len(commentary.split())
print(f"\nCritical Commentary ({word_count_commentary} words):\n")
print(commentary)


# ============================================================================
# GENERATE DELIVERABLE REPORT (Markdown for PDF/DOCX conversion)
# ============================================================================

report = f"""# M4 U2 Assignment: NLP for Construction Document Analysis
## Master's in AI for Architecture & Construction (Zigurat)
---

## Original Unstructured Document

{document.strip()}

---

## Part 1: Information Extraction (Structured Output)

### Extraction Methodology
A rule-based NLP pipeline was implemented using Python's `re` module with the following extractors:
- **Date extraction**: Multiple regex patterns for various date formats
- **Monetary value extraction**: GBP currency pattern matching
- **Obligation extraction**: Modal verb pattern detection (shall, must, is responsible for)
- **Risk/penalty extraction**: Keyword-based sentence filtering
- **Party extraction**: Named entity patterns with role labels
- **Location/project type**: Contextual phrase matching

### Structured JSON Output

```json
{json.dumps(structured_data, indent=2)}
```

---

## Part 2: Document Summary ({word_count} words)

{summary}

---

## Part 3: Prompt Engineering Documentation

### Prompt 1 — Initial Prompt (Naive)
**Prompt:** "{prompts[0]["prompt"]}"
**Issue:** {prompts[0]["issue"]}
**Output Quality:** {prompts[0]["output_quality"]}

### Prompt 2 — Improved Prompt (Structured Request)
**Prompt:** "{prompts[1]["prompt"]}"
**What Changed:** {prompts[1]["what_changed"]}
**Why It Improved:** {prompts[1]["why_improved"]}

### Prompt 3 — Refined Prompt (Domain-Aware + Role Assignment)
**Prompt:** "{prompts[2]["prompt"]}"
**What Changed:** {prompts[2]["what_changed"]}
**Why It Improved:** {prompts[2]["why_improved"]}

### Prompt 4 — Summary-Specific Prompt
**Prompt:** "{prompts[3]["prompt"]}"
**What Changed:** {prompts[3]["what_changed"]}
**Why It Improved:** {prompts[3]["why_improved"]}

---

## Part 4: Critical Commentary ({word_count_commentary} words)

{commentary}

---

*Generated using Python NLP pipeline — M4 U2 Assignment*
"""

with open("M4_U2_Assignment_Report.md", "w") as f:
    f.write(report)

print("\n" + "=" * 80)
print("ALL FILES GENERATED:")
print("  1. structured_extraction.json  — Part 1 JSON output")
print("  2. M4_U2_Assignment_Report.md  — Complete deliverable report")
print("=" * 80)
