import pandas as pd
import csv
from datetime import datetime


class CSV:
    CSV_FILE = "finance_data.csv"

    # Initialize the CSV file
    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            # A DataFrame is an object within pandas that allows us to access different rows/columns from a CSV file
            df = pd.DataFrame(
                columns=["date", "amount", "category", "description"])
            # The code below will write the DataFrame to the CSV file
            df.to_csv(cls.CSV_FILE, index=False)

    # Add some entries to the CSV file
    @classmethod
    def add_entry(cls, amount, category, description):
        new_entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }


CSV.initialize_csv()
