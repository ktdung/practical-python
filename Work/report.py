# report.py
#
# Exercise 2.4: A list of tuples
import csv

def read_portfolio(filename):
  '''Reads a portfolio file and returns a list of (name, shares, price) tuples'''
  portfolio = []

  with open(filename, 'rt') as file:
    rows = csv.reader(file)
    next(rows)
    for row in rows:
      try:
        hoding = (row[0], int(row[1]), float(row[2]))
        portfolio.append(hoding)
      except ValueError:
        print('Error: There was a problem with the data format in the file.')
        continue
  return portfolio