# app/benchmarking.py

import csv
import os

def get_benchmark(sector, geography):
    """
    Retrieves benchmark data from a local CSV file using a reliable path.
    """
    # Get the absolute path to the directory of the current script (benchmarking.py)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the file path relative to the script's directory
    file_path = os.path.join(script_dir, "..", "data", "benchmark_data.csv")
    
    # Check if the file exists before attempting to open
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Benchmark data file not found at: {file_path}")

    with open(file_path, mode='r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if row['sector'] == sector and row['geography'] == geography:
                return {
                    "avg_churn_rate": float(row['avg_churn_rate']),
                    "avg_market_size": float(row['avg_market_size']),
                }
    
    return None
