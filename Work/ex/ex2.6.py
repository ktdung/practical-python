# Exercise 2.6: Dictionaries as a container


import csv

def read_prices(filename):
  '''Reads a price file and returns a dictionary of {name: price} pairs'''
  prices = {}

  with open(filename, 'rt') as file:
    rows = csv.reader(file)
    for row in rows:
      if len(row) == 0:
        continue
      try:
        name = row[0].strip().strip('"')
        price = float(row[1])
        prices[name] = price
      except ValueError:
        print('Error: There was a problem with the data format in the file.')
        continue
  return prices