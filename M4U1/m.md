# M4U1 Assignment Solution: Predictive Engine for AECO
## Recommended Dataset
The **UCI Energy Efficiency Dataset** is the ideal choice for this assignment. It contains **768 building configurations** with 8 input features (building geometry parameters) and 2 target variables (Heating Load and Cooling Load). The dataset was created by Tsanas & Xifara (2012) using Ecotect simulation software on 12 different building shapes, published in *Energy and Buildings*, Vol. 49.[^1][^2][^3]

**Download link:** https://archive.ics.uci.edu/dataset/242/energy+efficiency[^2]
### Why This Dataset?
- **Directly AECO-relevant:** It models building energy performance from design parameters (compactness, surface area, wall area, roof area, height, orientation, glazing) — exactly the type of data an AECO firm would have in historical spreadsheets[^1][^2]
- **Clean and ML-ready:** No missing values, 768 rows, proper numerical features — ideal for a model competition[^2]
- **Peer-reviewed:** Published in a respected journal, giving academic credibility to the assignment[^3]
- **Regression task:** Predicting continuous values (kWh/m²) aligns perfectly with the brief's request for a "Predictive Engine"

***
## Alternative Datasets (If You Want Something Different)
| Dataset | Source | Rows | Use Case |
|---------|--------|------|----------|
| **Energy Efficiency** (recommended) | UCI ML Repository [^2] | 768 | Predict heating/cooling loads from building geometry |
| **Real Estate Valuation** | Kaggle [^4] | 414 | Predict property prices from age, distance to transit, nearby stores |
| **Construction Project Management** | Kaggle [^5] | 1,300 | Predict project delays/performance from planning variables |
| **Building Performance Dataset** | Kaggle [^6] | ~5,000 | Predict construction performance metrics |

***
## Model Results Summary
![](https://ppl-ai-code-interpreter-files.s3.amazonaws.com/web/direct-files/cbc7b14e1306f0ae8f32fb2dc03872cf/84f7a6a9-1c3e-4595-aa6c-b65df9a40c06/552cb01d.png)
The analysis trained **Linear Regression** (Model A) and **Random Forest Regressor** (Model B) on the Energy Efficiency dataset to predict **Heating Load (Y1)**.

| Metric | Linear Regression | Random Forest (Default) | Random Forest (Tuned) |
|--------|------------------|------------------------|----------------------|
| **R² Score** | 0.9122 | 0.9977 | 0.9977 |
| **RMSE (kWh/m²)** | 3.03 | 0.49 | 0.49 |
| **MAE (kWh/m²)** | 2.18 | 0.35 | 0.35 |
![](https://ppl-ai-code-interpreter-files.s3.amazonaws.com/web/direct-files/cbc7b14e1306f0ae8f32fb2dc03872cf/84f7a6a9-1c3e-4595-aa6c-b65df9a40c06/a2ea1d25.png)

**Winner: Random Forest Regressor** — It captures non-linear interactions between building geometry features that Linear Regression misses, achieving 6× lower prediction error.
### Hyperparameter Tuning Results
GridSearchCV with 5-fold cross-validation identified the best Random Forest configuration:
- `n_estimators`: 200
- `max_depth`: 15
- `min_samples_split`: 2
- `min_samples_leaf`: 1

The default RF was already near-optimal, confirming the model's robustness.
### Feature Importance
![](https://ppl-ai-code-interpreter-files.s3.amazonaws.com/web/direct-files/cbc7b14e1306f0ae8f32fb2dc03872cf/84f7a6a9-1c3e-4595-aa6c-b65df9a40c06/5dafe254.png)

Relative Compactness (39.8%) and Surface Area (21.0%) dominate heating load prediction, aligning with thermodynamic principles — compact buildings with less surface area lose less heat.
### Actual vs Predicted
![](https://ppl-ai-code-interpreter-files.s3.amazonaws.com/web/direct-files/cbc7b14e1306f0ae8f32fb2dc03872cf/84f7a6a9-1c3e-4595-aa6c-b65df9a40c06/a93aaade.png)

---
## Deliverables
### 1. Jupyter Notebook (.ipynb)
The complete notebook includes all required sections: data loading, cleaning, EDA with correlation heatmaps, training Model A (Linear Regression), training Model B (Random Forest), hyperparameter tuning with GridSearchCV, and a final comparison table with visualisations.
### 2. Analyst Report (Markdown)
A full business report explaining: dataset selection rationale, algorithm choices, results interpretation, feature importance analysis, and a clear business recommendation for the AECO firm.
### 3. Model Comparison CSV
---
## How to Run the Notebook
1. Open the `.ipynb` file in Jupyter Notebook, Google Colab, or VS Code
2. Run all cells in order — the dataset downloads automatically from the UCI repository
3. Required libraries: `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`, `openpyxl`
4. Install if needed: `pip install pandas numpy scikit-learn matplotlib seaborn openpyxl`

***
## Rubric Alignment
### Scenario Complexity
- Uses a **real-world, peer-reviewed dataset** from the UCI ML Repository (not synthetic)[^2]
- Implements **two fundamentally different algorithms** (parametric vs. ensemble)
- Performs **hyperparameter tuning** with GridSearchCV and 5-fold cross-validation
- Includes **feature importance analysis** for business insights
### Reasoning
- Clearly explains **why** this dataset was chosen (AECO relevance, building performance, energy costs)
- Justifies **why** each algorithm was selected (simplicity baseline vs. non-linear complexity capture)
- Provides **actionable business recommendations** (deploy RF for pre-construction energy estimation)
- All work is **reproducible** with fixed random seeds and direct data download from UCI[^3]

---

## References

1. [elifkavak/energy-efficiency-dataset](https://github.com/elifkavak/energy-efficiency-dataset) - Source: UCI Machine Learning Repository, “Energy Efficiency” dataset (https://archive.ics.uci.edu/da...

2. [Energy Efficiency](https://archive.ics.uci.edu/dataset/242/energy+efficiency) - Discover datasets around the world!

3. [Energy Efficiency - UCI Machine Learning Repository](https://archive-beta.ics.uci.edu/dataset/242/energy+efficiency) - This study looked into assessing the heating load and cooling load requirements of buildings (that i...

4. [Real Estate Dataset](https://www.kaggle.com/datasets/sumelahmad/real-estate) - Real Estate Market Analysis: Property Pricing Factors

5. [Predictive Analytics on the Construction Project - Kaggle](https://www.kaggle.com/code/salemnka/predictive-analytics-on-the-construction-project) - ... Kaggle Notebooks | Using data from Construction Project Management Dataset. ... Dataset Shape: (...

6. [Building Performance Dataset](https://www.kaggle.com/datasets/ziya07/construction-project-performance-dataset/code) - predicting construction performance using deep learning models

