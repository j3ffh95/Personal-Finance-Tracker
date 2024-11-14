import pandas as pd
import csv
from datetime import datetime
from data_entry import get_amount, get_category, get_date, get_description


class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["date", "amount", "category", "description"]
    FORMAT = "%m-%d-%Y"

    # Initialize the CSV file
    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            # A DataFrame is an object within pandas that allows us to access different rows/columns from a CSV file
            df = pd.DataFrame(
                columns=cls.COLUMNS)
            # The code below will write the DataFrame to the CSV file
            df.to_csv(cls.CSV_FILE, index=False)

    # Add some entries to the CSV file
    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }
        # Create CSV writer
        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Entry added successfully!")

    @classmethod
    def get_transactions(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE)


def add():
    CSV.initialize_csv()
    date = get_date(
        "Enter the date of the transaction (mm-dd-yyyy) or enter for today's date: ", allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category, description)


add()
