# Master's in AI for Architecture and Construction (MAICEN-1125)

![Institution](https://img.shields.io/badge/Institution-Zigurat%20Institute%20of%20Technology-blue)
![Course](https://img.shields.io/badge/Course-MAICEN--1125-green)

This repository contains the assignments for the **Master's in AI for Architecture and Construction** program at the **Zigurat Institute of Technology**. Each module's project is organized into its own directory, containing all relevant code, documentation, and resources.

## Repository Structure

The repository is organized by course modules. Each module's folder contains the assignment(s) for that unit.

```
.
├── M2U1/           # FIDIC Notice Generator
├── M2U2/           # Project Data Handling with Python
├── M2U3/           # RAG Mini Project (n8n)
├── M4U1/           # Predictive Engine for Building Energy Efficiency
├── M4U2/           # NLP for Construction Document Analysis
└── README.md
```

## Assignments Overview

| Module          | Assignment Title                                 | Description                                                                                                                                                     |
| :-------------- | :----------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [M2U1](./M2U1/) | FIDIC Notice Generator                           | A tool to automate the generation of FIDIC notices based on contract conditions.                                                                                |
| [M2U2](./M2U2/) | Project Data Handling with Python                | A Python script for analyzing project cost data, highlighting overruns and delays.                                                                              |
| [M2U3](./M2U3/) | RAG Mini Project (n8n)                           | A simple RAG-style workflow that loads project data, filters relevant subsets, and answers using only retrieved context.                                        |
| [M4U1](./M4U1/) | Predictive Engine for Building Energy Efficiency | Supervised ML pipeline (Linear Regression vs Random Forest) to predict Heating Load from building geometry. Random Forest achieved R² = 0.9977.                 |
| [M4U2](./M4U2/) | NLP for Construction Document Analysis           | Rule-based NLP pipeline to extract structured data from an unstructured construction contract, with summarisation, prompt engineering, and critical commentary. |

## Running the Code

Ensure UV is installed in your Python environment:

```bash
pip install uv
```

Install dependencies for each module by navigating to the respective directory and running:

```bash
uv install
```

### M2U1: FIDIC Notice Generator

### M2U2: Project Data Handling with Python

```bash
streamlit run M2U2/main.py
```

### M2U3: RAG Mini Project (n8n)

### M4U1: Predictive Engine

```bash
jupyter notebook M4U1/M4U1_Predictive_Engine.ipynb
```

### M4U2: NLP Pipeline

```bash
python3 M4U2/m4_u2_nlp_assignment_02.py
```

## About the Author

This repository is maintained by **Osama Ata**.

- GitHub: [osama-ata](https://github.com/osama-ata)
- LinkedIn: [Connect on LinkedIn](https://www.linkedin.com/in/osama-ata/)

---

_This repository is for educational purposes as part of the MAICEN-1125 program._
