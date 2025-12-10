"""
  Python script that:
- Loads structured project data (CSV).
- Calculates total cost per site (materials + labour).
- Compares actual vs. estimated values.
- Highlights sites where the budget or timeline is exceeded.
"""

import pandas as pd

input_file = "M2U2/project_data.csv"
output_file = "M2U2/summary_report.txt"


def main():
    # Load structured project data from CSV
    data = pd.read_csv(input_file)

    # Calculate total cost per site
    data["estimated_total_cost"] = (
        data["estimated_materials_cost"] + data["estimated_labor_cost"]
    )
    data["actual_total_cost"] = (
        data["actual_materials_cost"] + data["actual_labor_cost"]
    )

    # Compare actual vs. estimated values
    data["cost_overrun"] = data["actual_total_cost"] - data["estimated_total_cost"]
    data["timeline_delay"] = (
        data["actual_duration_days"] - data["estimated_duration_days"]
    )

    # Highlight sites where the budget or timeline is exceeded
    over_budget_sites = data[data["cost_overrun"] > 0]
    delayed_sites = data[data["timeline_delay"] > 0]

    print("--- Project Cost Summary Report ---")
    print("\nSites Over Budget:")
    print(
        over_budget_sites[
            [
                "site_name",
                "estimated_total_cost",
                "actual_total_cost",
                "cost_overrun",
            ]
        ]
    )

    print("\nSites with Timeline Delays:")
    print(
        delayed_sites[
            [
                "site_name",
                "estimated_duration_days",
                "actual_duration_days",
                "timeline_delay",
            ]
        ]
    )

    # Optional: Export summary report to .txt or .csv
    with open(output_file, "w") as f:
        f.write("--- Project Cost Summary Report ---\n")
        f.write("\nSites Over Budget:\n")
        f.write(
            over_budget_sites[
                [
                    "site_name",
                    "estimated_total_cost",
                    "actual_total_cost",
                    "cost_overrun",
                ]
            ].to_string()
        )
        f.write("\n\nSites with Timeline Delays:\n")
        f.write(
            delayed_sites[
                [
                    "site_name",
                    "estimated_duration_days",
                    "actual_duration_days",
                    "timeline_delay",
                ]
            ].to_string()
        )

    print("\nSummary report also saved to summary_report.txt")


if __name__ == "__main__":
    main()
