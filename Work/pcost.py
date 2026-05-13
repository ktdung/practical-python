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
# Exercise 2.15: A practical enumerate() example

import sys
import report
def portfolio_cost(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    portfolio = report.read_portfolio(filename)
    return sum(stock.cost() for stock in portfolio)


# if len(sys.argv) == 2:
#   filename = sys.argv[1]
# else:
#   # filename = 'Data/missing.csv'
# #   filename = 'Data/portfolio.csv'
#     filename = input('Enter the portfolio filename: ')

# cost = portfolio_cost(filename)
# print('Total cost:', cost)

def main(args):
   if len(args) != 2:
      raise SystemExit(f'Usage: {args[0]} portfolio-file')
   filename = args[1]
   cost = portfolio_cost(filename)
   print('Total cost:', cost)

if __name__ == '__main__':
  import sys
  main(sys.argv)

