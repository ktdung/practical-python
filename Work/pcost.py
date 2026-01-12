# pcost.py
#
# Exercise 1.27
# with open("Data/portfolio.csv", 'rt') as file:
#   total_cost = 0.0
#   next(file)
#   for line in file:
#     parts = line.split(',')
#     shares = int(parts[1])
#     price = float(parts[2])
#     total_cost += shares * price
#   print(f'Total cost: {total_cost}')

# Exercise 1.28
# import gzip

# with gzip.open("Data/portfolio.csv.gz", "rt") as file:
#   for line in file:
#     print(line, end='')


# Exercise 1.30
# def portfolio_cost(filename):
#   total_cost = 0.0
#   with open(filename, 'rt') as file:
#     next(file)
#     for line in file:
#       parts = line.split(',')
#       try:
#         shares = int(parts[1])
#         price = float(parts[2])
#       except ValueError:
#         print('Error: There was a problem with the data format in the file.')
#         continue
#       total_cost += shares * price
#   return total_cost

# cost = portfolio_cost('Data/missing.csv')
# print('Total cost:', cost)

# Exercise 1.32: Using a library function
import csv
def portfolio_cost(filename):
  total_cost = 0.0
  with open(filename, 'rt') as file:
    reader = csv.reader(file)
    next(reader)
    for parts in reader:
      try:
        shares = int(parts[1])
        price = float(parts[2])
      except ValueError:
        print('Error: There was a problem with the data format in the file.')
        continue
      total_cost += shares * price
  return total_cost

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)