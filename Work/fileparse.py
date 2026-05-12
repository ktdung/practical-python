# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(filename, select=None):
    """
    Parse a CSV file into a list of records
    """
    with open(filename) as f:
        rows = csv.reader(f)

        # Read the file headers
        headers = next(rows)

        # If a column selector was given, find indices of the specified columns
        # Also narrow the set of headers useds for resuulting dictionaries

        if select:
            indicies = [headers.index(colname) for colname in select]
            headers = select
        else:
            indicies = []

        records = []
        for row in rows:
            if not row:  # Skip rows with now data
                continue

            # Filter the row if specific columns were selected
            if indicies:
                row = [row[index] for index in indicies]

            # Make a dictionary for the row and add it to the records list
            record = dict(zip(headers, row))
            records.append(record)

        return records
