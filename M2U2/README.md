# M2U2 | Individual Assignment: Project Cost Analysis Tool

An interactive web application built with Streamlit to analyze project data from a CSV file. It calculates cost overruns, identifies timeline delays, and presents the findings in a user-friendly interface.

## Features

- **Interactive Data Loading**: Upload project data via a web interface (`project_data.csv`).
- **Cost Calculation**: Computes total estimated vs. actual costs for materials and labor.
- **Variance Analysis**: Compares estimated and actual values to identify cost overruns and timeline delays.
- **Reporting**:
  - Displays a summary report in the web application.
  - Allows for downloading the detailed report.

## Requirements

- Python 3.x
- pandas
- streamlit

You can install the necessary libraries using pip:

```bash
pip install pandas streamlit
```

## How to Run

1. **Ensure your data is ready**: Have your `project_data.csv` file ready for upload. The CSV should have the following columns:
    - `site_id`
    - `site_name`
    - `estimated_materials_cost`
    - `actual_materials_cost`
    - `estimated_labor_cost`
    - `actual_labor_cost`
    - `estimated_duration_days`
    - `actual_duration_days`

2. **Execute the application**: Run the `main.py` script using Streamlit from your terminal:

    ```bash
    streamlit run M2U2/main.py
    ```

## Output

The script will launch a web application in your browser, where you can see the project cost analysis, including sites that are over budget and those with timeline delays.
