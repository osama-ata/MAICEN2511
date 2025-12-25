"""
Docstring for M2U3.csv_to_json

This module provides functionality to convert CSV files to JSON format.
"""

import csv
import json
import os
from typing import Any


def infer_type(value: str) -> Any:
    """
    Convert a string value to int or float when possible, otherwise return the original string.
    Empty strings are converted to None.
    """
    if value is None:
        return None
    v = value.strip()
    if v == "":
        return None
    # Try int first, then float, otherwise keep as string
    try:
        return int(v)
    except ValueError:
        try:
            return float(v)
        except ValueError:
            return v


def csv_to_json(csv_file_path: str, json_file_path: str) -> None:
    """
    Convert a CSV file to JSON format with simple type inference for each cell.

    Parameters:
    csv_file_path (str): The path to the input CSV file.
    json_file_path (str): The path to the output JSON file.
    """
    # Check if the CSV file exists
    if not os.path.exists(csv_file_path):
        raise FileNotFoundError(f"The file {csv_file_path} does not exist.")

    # Read the CSV file and convert to JSON with type inference
    with open(csv_file_path, mode="r", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = []
        for row in csv_reader:
            typed_row = {k: infer_type(v) for k, v in row.items()}
            data.append(typed_row)

    # Write the JSON data to the output file
    with open(json_file_path, mode="w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4)


if __name__ == "__main__":
    csv_file_path = "M2U3/project_data.csv"
    json_file_path = "M2U3/project_data.json"
    csv_to_json(csv_file_path, json_file_path)
