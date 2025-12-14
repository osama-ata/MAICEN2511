"""
  Python script that:
- Loads structured project data (CSV).
- Calculates total cost per site (materials + labour).
- Compares actual vs. estimated values.
- Highlights sites where the budget or timeline is exceeded.
"""

import streamlit as st
import pandas as pd

# input_file = "M2U2/project_data.csv"

output_file = "M2U2/summary_report.txt"


def main():
    st.title("Project Data Handling with Python")

    # Streamlit file uploader for CSV input
    input_file = st.file_uploader(
        "upload projects data CSV file", type="CSV", accept_multiple_files=False
    )

    # Load structured project data from CSV
    if input_file is not None:
        df = pd.read_csv(input_file)

        # Calculate total cost per site
        df["estimated_total_cost"] = (
            df["estimated_materials_cost"] + df["estimated_labor_cost"]
        )
        df["actual_total_cost"] = df["actual_materials_cost"] + df["actual_labor_cost"]

        # Compare actual vs. estimated values
        df["cost_overrun"] = df["actual_total_cost"] - df["estimated_total_cost"]
        df["timeline_delay"] = (
            df["actual_duration_days"] - df["estimated_duration_days"]
        )

        # Highlight sites where the budget or timeline is exceeded
        over_budget_sites = df[df["cost_overrun"] > 0]
        delayed_sites = df[df["timeline_delay"] > 0]

        # Generate summary report

        st.write("\nSites Over Budget:")
        st.write(
            over_budget_sites[
                [
                    "site_name",
                    "estimated_total_cost",
                    "actual_total_cost",
                    "cost_overrun",
                ]
            ]
        )

        st.write("\nSites with Timeline Delays:")
        st.write(
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
        summary_report = "--- Project Cost Summary Report ---\n"
        summary_report += "\nSites Over Budget:\n"
        summary_report += over_budget_sites[
            [
                "site_name",
                "estimated_total_cost",
                "actual_total_cost",
                "cost_overrun",
            ]
        ].to_string()
        summary_report += "\n\nSites with Timeline Delays:\n"
        summary_report += delayed_sites[
            [
                "site_name",
                "estimated_duration_days",
                "actual_duration_days",
                "timeline_delay",
            ]
        ].to_string()

        st.download_button(
            label="Download Summary Report",
            data=summary_report,
            file_name="summary_report.txt",
            mime="text/plain",
        )


if __name__ == "__main__":
    main()

    # Display the uploaded data
    st.write(df)

    helper_function(df)


if __name__ == "__main__":
    main()
