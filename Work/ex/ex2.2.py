# Exercise 2.2: Dictionaries as a data structure
import csv

f = open('../Data/portfolio.csv', 'r')
rows = csv.reader(f)
header = next(rows)
row = next(rows)
d = {
  'name': row[0],
  'shares': int(row[1]),
  'price': float(row[2])
}
print(f"{d['shares'] * d['price']:0.2f}")