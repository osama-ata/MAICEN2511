"""
Docstring for M2U3.csv_to_json

This module provides functionality to convert CSV files to JSON format.
"""

import csv
import json
import os


def csv_to_json(csv_file_path: str, json_file_path: str) -> None:
    """
    Convert a CSV file to JSON format.

    Parameters:
    csv_file_path (str): The path to the input CSV file.
    json_file_path (str): The path to the output JSON file.
    """
    # Check if the CSV file exists
    if not os.path.exists(csv_file_path):
        raise FileNotFoundError(f"The file {csv_file_path} does not exist.")

    # Read the CSV file and convert to JSON
    with open(csv_file_path, mode="r", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = [row for row in csv_reader]

    # Write the JSON data to the output file
    with open(json_file_path, mode="w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4)


csv_file_path = "M2U3/project_data.csv"
json_file_path = "M2U3/project_data.json"
csv_to_json(csv_file_path, json_file_path)
