# M2U3 — Individual Assignment: RAG Mini Project

Goal

- Build a simple RAG (Retrieval-Augment-Generation) workflow (n8n or any tool).
- Let an AI answer questions based only on your own data: upload a file, search it, and have the AI answer using only matched content.

Deliverables

1. A working no-code RAG workflow exported as JSON + screenshots.
2. 3–6 screenshots (one per node).
3. One short sentence per node describing its job (e.g., “This node loads my CSV file.”).
4. A short reflection (max 500 words) including:
   - What the data is.
   - What questions people will ask.
   - What the AI should reply with.
   - Notes on: why clean data matters, why filtering is “search before generate,” how RAG reduces hallucination, what was easy vs. confusing.

Features / Flow

1. Load your file.
2. Search for rows that match the question.
3. Provide those rows as context to the AI.
4. AI answers using only that data.

RAG prompt

```text
Answer only using the data below.
DATA:
{{context}}
QUESTION:
{{query}}
If the answer is not in the data, reply exactly: "No information available."
```

Notes / Tips

- Keep your data clean and well-structured (columns, consistent formatting) to improve retrieval accuracy.
- Filtering relevant rows before generation reduces hallucination by constraining the model to source content.
- Use short, factual answers where appropriate and cite the row or source if helpful.

## Example summary (for reflection)

- Data: [CSV](project_data.csv), [JSON](M2U3/project_data.json) about construction sites having these columns:
  - `site_id`
  - `site_name`
  - `estimated_materials_cost`
  - `actual_materials_cost`
  - `estimated_labor_cost`
  - `actual_labor_cost`
  - `estimated_duration_days`
  - `actual_duration_days`

- People will ask: which sites are over budget, delayed, or completed?
- Questions: cost, properties, or availability.
- AI replies: short factual answers drawn from the data only.

## Workflow overview (small)

- Load file: Ingest the uploaded CSV/JSON into the workflow.
- Search: Find top matching rows for the user query.
- Context assembly: Combine matched rows into the DATA block for the RAG prompt.
- Generate answer: Run the LLM with the prompt "Answer only using the data below..." and return the model response (or "No information available." if no match).
