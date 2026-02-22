## 1. Prompt to Help You Choose a Suitable Dataset

#### Prompt 1 - Find and justify an AECO-related dataset

**Prompt:**

I am working on an assignment as a Data Analyst in a large AECO (Architecture, Engineering, Construction and Operations) company.
My task is to:

- Select a **public dataset** relevant to **construction, real estate, or building performance** .
- Build at least **two different Machine Learning models** to predict a numerical or categorical project outcome (e.g., cost, delay, energy use, price, risk).
- Compare the models and then optimise the best-performing one.

Help me by:

1. Suggesting **3-5 concrete public datasets** (with links if possible) that are:
    - Related to construction, real estate, or building performance
    - Have enough rows (ideally &gt; 500) and several features (numerical + categorical)
    - Suitable for a **supervised learning task** (regression or classification).
2. For each suggested dataset, explain in **2-3 sentences** :
    - Why it is relevant to AECO
    - What potential **prediction task** it supports (e.g., predict housing price, energy consumption, project delay).
3. Finally, recommend **one dataset as the best choice** for this assignment and clearly justify:
    - Why it offers a meaningful business problem
    - Why it is suitable for comparing at least two ML models.

Answer in a structured Markdown format with headings and bullet points so I can quickly choose one.

**Purpose:** To help you quickly pick a realistic AECO-related dataset **and** already have a justification for your report.

**Why this is a good prompt:**

- Clear **goal** : find a dataset that fits assignment constraints.
- Rich **context** : mentions AECO, ML models, supervised learning.
- Defines **selection criteria** : size, relevance, type of target variable.
- Sets **expectations** : structured answer, justification, recommendation.

### 2. Prompt for Initial Data Exploration and Cleaning (in Jupyter)

Once you have your dataset and load it into a pandas DataFrame (say df), you can ask Copilot to guide you through cleaning.

#### Prompt 2 - EDA and data cleaning plan

**Prompt:**

I have loaded a dataset into a pandas DataFrame called df in a Jupyter Notebook.
The dataset is about [briefly describe, e.g., â€œresidential building energy performanceâ€ or â€œreal estate pricesâ€].
My assignment requires me to:

- Show **data loading and cleaning**
- Build at least **two ML models on the same data**
- Compare their performance and optimise the best one.

Please:

1. Propose a clear **Exploratory Data Analysis (EDA) and data cleaning plan** for this dataset, including:
    - Overview checks (shape, dtypes, head, summary statistics)
    - Missing value analysis
    - Outlier detection (at least simple checks)
    - Handling of categorical vs numerical features
    - Basic feature engineering if helpful (e.g., encoding, scaling, new derived features).
2. Suggest which columns could be good **features (X)** and which one should be the **target (y)** for a supervised ML task relevant to AECO business decisions.
3. Provide **Python code snippets** using pandas, matplotlib/seaborn, and scikit-learn to implement the main steps.

Keep the explanations concise but clear, so I understand *why* each step is done (I will adapt the code myself).

**Purpose:** To get a **roadmap + starter code** for EDA and cleaning, while still leaving you in control.

**Why this is a good prompt:**

- Gives Copilot **context** (assignment requirements + dataset theme).
- Asks for both **plan** and **code** , and for explanations (important for your â€œReasoningâ€ rubric).
- Keeps you as the decision-maker (â€œI will adapt the code myselfâ€).

### 3. Prompt to Build Two Competing Models

You need at least two algorithms. A common and sensible pairing:

- **Model A** : Linear Regression (or Logistic Regression for classification)
- **Model B** : Random Forest (regressor or classifier)

#### Prompt 3 - Implement two models and compare them

**Prompt:**

I am working in a Jupyter Notebook with a cleaned dataset stored in X (features) and y (target).
My assignment requires a **â€œmodel competitionâ€** :

- Train **two different ML algorithms** on the same data
- Compare their performance using appropriate metrics
- Decide which model is better for the AECO business problem.

For this dataset:

- Assume it is a [regression/classification] problem.
- I want to try **Model A: [LinearRegression or LogisticRegression]** and **Model B: [RandomForestRegressor or RandomForestClassifier]** from scikit-learn.

Please help me with:

1. A clear train/test split using train\_test\_split.
2. Training and evaluating both models using:
    - Appropriate metrics (e.g., MAE, RMSE, RÂ² for regression; accuracy, precision, recall, F1 for classification).
    - Cross-validation if appropriate.
3. Code to print **side-by-side comparison** of model performance.
4. Brief comments (as Markdown-style text or inline comments) explaining:
    - Why these metrics make sense for this task
    - How to interpret which model is â€œbetterâ€ in business terms (e.g., error in predicted cost or energy).

Provide the code in well-structured cells with clear comments so that the work looks professional and reproducible.

**Purpose:** To generate a clean, reproducible comparison between two models that fits exactly what your brief requires.

**Why this is a good prompt:**

- Very clear about **which** models to use.
- Specifies the **evaluation criteria** and business interpretation.
- Mentions **professional and reproducible** , aligning with your rubric.

### 4. Prompt for Optimising the â€œWinningâ€ Model

Once you see which model performs better, you must **optimise** it (e.g., change tree depth, number of trees, regularisation, etc.).

#### Prompt 4 - Hyperparameter tuning of the best model

**Prompt:**

I have compared two models on the same dataset:

- Model A: [e.g., LinearRegression]
- Model B: [e.g., RandomForestRegressor]

Based on initial results, **Model B is performing better** according to [state the main metric, e.g., lower RMSE / higher RÂ² / better F1].
Now I need to:

- **Optimise Model B** using hyperparameter tuning
- Show in my assignment how tuning improved (or not) the performance.

Please:

1. Suggest **which hyperparameters** of [Model B name] are most relevant to tune for this kind of problem (e.g., n\_estimators, max\_depth, min\_samples\_split, etc.).
2. Provide scikit-learn code to run either:
    - GridSearchCV, or
    - RandomizedSearchCV
to search over a reasonable set of hyperparameters (not too huge for an assignment).
3. Show how to:
    - Fit the tuned model on the training data
    - Evaluate it on the test data with the same metrics as before
    - Compare performance **before vs after** tuning.
4. Include brief Markdown-style explanations on:
    - The intuition of the most important hyperparameters
    - Whether tuning meaningfully improved the model and why that matters for AECO decision-making.

Code should be clear, commented, and structured so that I can paste it into my Notebook and adapt it.

**Purpose:** To get structured hyperparameter tuning that you can easily adapt, and a before/after comparison for your report.

**Why this is a good prompt:**

- Focuses Copilot on the **best model only** , as required.
- Asks for both **technical steps** and **business interpretation** .
- Specifies the tool (GridSearchCV or RandomizedSearchCV) and type of output.

### 5. Prompt for Generating Plots and Visuals for the Notebook

Graphs help your notebook look more analytical and professional.

#### Prompt 5 - Visual analysis and model diagnostics

**Prompt:**

In my Jupyter Notebook, I would like to add **visualisations** that support my analysis and model comparison.
The dataset is about [short AECO context, e.g., building energy use, housing prices, project delays], and I have trained two models: [Model A] and [Model B].

Please propose and provide Python code for:

1. Basic EDA plots (using matplotlib or seaborn), such as:
    - Distribution of the target variable y
    - Correlation heatmap for numerical features
    - A few meaningful feature vs target scatter plots / box plots.
2. Model performance plots, such as:
    - For regression: predicted vs actual scatter plot, residual plot
    - For classification: confusion matrix, ROC curve (if applicable).
3. Short Markdown-style text to accompany each plot explaining:
    - What the plot shows
    - How it supports the choice between the two models or helps understand limitations.

Make sure the code is neatly formatted, with titles, axis labels, and legends so the Notebook looks professional.

**Purpose:** To generate ready-to-use visualisations and explanations that strengthen your reasoning and professionalism scores.

**Why this is a good prompt:**

- Explicitly connects visuals to **interpretation** and **model comparison** .
- Ensures your notebook doesnâ€™t just have code, but also clear communication.

### 6. Prompt to Draft the Analyst Report (PDF/Markdown)

Once your analysis is done, youâ€™ll need to write the **Analyst Report** . You can draft it in Word or Markdown, then export to PDF yourself.

#### Prompt 6 - Draft the business-style analyst report

Use this in **Word or a Markdown editor with Copilot** after your notebook is done.

**Prompt:**

I need to write an **Analyst Report** for a board-level audience in an AECO firm. The report must be simple, non-technical, and based on the work I have done in my Jupyter Notebook.

My assignment requirements for the report are:

- Explain **why I chose this dataset** and why it is relevant to AECO.
- Explain **why I chose these two algorithms** , for example, one simpler and one more complex / non-linear.
- State **which model is best for this application** and why, in business terms.
- Report the **final accuracy/error metrics** in a way that a non-technical audience can understand.
- Show that I understand **why** we are doing this and what decisions it supports.

I will now paste key information from my analysis:

1. A short description of the dataset and target variable
2. A short summary of the two models, their main settings, and evaluation metrics
3. Notes on which model performed better and the results after optimisation.

Using that information, please help me draft a **professional, concise Analyst Report** with the following structure:

- Executive Summary (no more than 2-3 short paragraphs)
- Dataset and Business Context (why this data matters to AECO)
- Modelling Approach (which algorithms and why)
- Results and Model Comparison (with simplified explanation of metrics)
- Optimisation and Final Recommendation (why the chosen model is preferred)
- Limitations and Next Steps (e.g., need for more data, additional features, or monitoring).

Use a clear, polite, and business-oriented tone. Avoid heavy technical jargon; where technical terms are necessary, briefly explain them in plain language. I will review and adjust the text to ensure it matches my own understanding and work.

**Purpose:** To turn your technical work into a **clear business report** aligned with the assignmentâ€™s questions.

**Why this is a good prompt:**

- Very clearly structured around the **assignment headings/questions** .
- Asks Copilot to write for a **board** audience, not engineers.
- Emphasises *you* will paste in the actual results (avoiding fabrication).

### 7. Prompt to Check Reproducibility and Professionalism

Before submitting, you can ask Copilot to review your notebookâ€™s clarity.

#### Prompt 7 - Review notebook for clarity and reproducibility

**Prompt:**

I have completed a Jupyter Notebook that:

- Loads and cleans a dataset
- Trains two ML models
- Compares their performance
- Tunes the best model

I want to maximise my grade on:

- **Scenario Complexity** (challenge level)
- **Reasoning** (showing I understand why Iâ€™m doing each step)
- **Reproducibility and professionalism** .

Please review the notebook code and Markdown cells (I will paste them in sections) and suggest improvements for:

1. Clarity of explanations: Where should I add or improve Markdown comments to better explain *why* I chose certain steps, models, and metrics?
2. Reproducibility: Are there any places where I should fix random seeds, show library versions, or make data paths more explicit?
3. Professional appearance: Suggestions for better structure, headings, or plot labelling.

Provide concrete suggestions and example wording for Markdown cells that I can insert above or below specific code cells.

**Purpose:** To â€œpolishâ€ your work so it looks coherent, thoughtful, and professional.

**Why this is a good prompt:**

- Targets your **rubric** directly.
- Focuses Copilot not on doing the work, but on **improving communication** .

### How to Use These Prompts Effectively

1. **Adapt, donâ€™t copy blindly** - Youâ€™ll get the best results if you tweak each prompt with:
    - The exact dataset you chose
    - Whether youâ€™re doing regression or classification
    - Any specific business angle (cost, delay, energy, price, etc.)
2. **Keep academic integrity** - Use Copilot as a partner:
    - You decide the target variable, final models, and interpretations.
    - You verify any code and write the final reasoning in your own words.
3. **Keep everything consistent** - The dataset description in the notebook and in the report should match the same story (e.g., predicting construction cost or building energy performance).