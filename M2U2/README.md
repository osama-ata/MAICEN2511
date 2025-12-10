# M2U2 | Individual Assignment: Project Cost Analysis Tool

A Python-based utility designed to analyze project data from a CSV file. It calculates cost overruns, identifies timeline delays, and generates a summary report.

## Features

- **Data Loading**: Reads project data from a specified CSV file (`project_data.csv`).
- **Cost Calculation**: Computes total estimated vs. actual costs for materials and labor.
- **Variance Analysis**: Compares estimated and actual values to identify cost overruns and timeline delays.
- **Reporting**:
  - Prints a summary report to the console.
  - Exports the detailed report to a text file (`summary_report.txt`).

## Requirements

- Python 3.x
- pandas

You can install the necessary library using pip:

```bash
pip install pandas
```

## How to Run

1. **Ensure your data is ready**: Place your `project_data.csv` file in the same directory as the script. The CSV should have the following columns:
    - `site_id`
    - `site_name`
    - `estimated_materials_cost`
    - `actual_materials_cost`
    - `estimated_labor_cost`
    - `actual_labor_cost`
    - `estimated_duration_days`
    - `actual_duration_days`

2. **Execute the script**: Run the `main.py` script from your terminal:

    ```bash
    python main.py
    ```

## Output

The script will generate two outputs:

1. **Console Output**: A summary report will be printed directly to your terminal, showing sites that are over budget and those with timeline delays.
2. **File Output**: A text file named `summary_report.txt` will be created in the same directory, containing the full report for your records.
