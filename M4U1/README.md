# M4U1 — Predictive Engine for Building Energy Efficiency

## Assignment Overview

**Module:** M4 Unit 1 — Data Analytics for AECO  
**Programme:** Master's in AI for Architecture & Construction (Zigurat)

This assignment builds a **supervised machine learning predictive engine** to forecast a building's **Heating Load (kWh/m²)** from design-stage geometric parameters. Two models are trained and compared — Linear Regression and Random Forest Regressor — with the goal of providing AECO firms with a pre-construction energy estimation tool.

---

## Files

| File                           | Description                                                 |
| ------------------------------ | ----------------------------------------------------------- |
| `M4U1_Predictive_Engine.ipynb` | Main Jupyter Notebook — full analysis, training, evaluation |
| `M4U1_Predictive_Engine.html`  | Static HTML export of the notebook                          |
| `M4U1_Predictive_Engine.pdf`   | PDF export of the notebook                                  |
| `M4U1_Analyst_Report.md`       | Written analyst report (Markdown source)                    |
| `M4U1_Analyst_Report.pdf`      | Analyst report (final PDF deliverable)                      |
| `datasets.md`                  | Dataset description and feature documentation               |
| `prompts.md`                   | Prompt engineering log used during the assignment           |

---

## Dataset

**UCI Energy Efficiency Dataset** — 768 building configurations × 10 variables  
Source: [UCI ML Repository](https://archive.ics.uci.edu/dataset/242/energy+efficiency)

| Input Features                                                                                                                 | Target                        |
| ------------------------------------------------------------------------------------------------------------------------------ | ----------------------------- |
| Relative Compactness, Surface Area, Wall Area, Roof Area, Overall Height, Orientation, Glazing Area, Glazing Area Distribution | **Y1: Heating Load (kWh/m²)** |

---

## Results Summary

| Model                     | R² Score   | RMSE            |
| ------------------------- | ---------- | --------------- |
| Linear Regression         | 0.9122     | 3.03 kWh/m²     |
| Random Forest (default)   | 0.9977     | 0.49 kWh/m²     |
| **Random Forest (tuned)** | **0.9977** | **0.49 kWh/m²** |

**Winner:** Random Forest — 99.8% variance explained, 6× lower error than Linear Regression.  
**Top predictor:** Relative Compactness (39.8% feature importance).

---

## Running the Notebook

Ensure dependencies are available (`pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`), then open the notebook:

```bash
jupyter notebook M4U1_Predictive_Engine.ipynb
```

Data is loaded directly from the UCI repository — no local dataset file required.

---

_M4U1 Assignment — MAICEN-1125 | Zigurat Institute of Technology_
