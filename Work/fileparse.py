# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=","):
    """
    Parse a CSV file into a list of records
    """
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        # Read the file headers has_headers is True, and use them as the keys for the dictionaries
        if has_headers:
            headers = next(rows)
        else:
            headers = []

        # If a column selector was given, find indices of the specified columns
        # Also narrow the set of headers useds for resuulting dictionaries

        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        records = []
        for row in rows:
            if not row:  # Skip rows with now data
                continue

            # Filter the row if specific columns were selected
            if select:
                row = [row[index] for index in indices]

            # Type conversion
            if types:
                row = [func(val) for func, val in zip(types, row)]

            # If no headers, create a tuple instead of a dictionary
            if not has_headers:
                record = tuple(row)
            else:
                # Make a dictionary for the row and add it to the records list
                record = dict(zip(headers, row))
            records.append(record)

        return records
