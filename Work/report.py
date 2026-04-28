# report.py
#
# Exercise 2.4: A list of tuples
# Exercise 2.5: List of Dictionaries
# Exercise 2.7: Finding out if you can retire
# Exercise 2.9: 2:11 Collecting Data

import csv

def read_portfolio(filename):
  '''Reads a portfolio file and returns a list of dictionaries
    with keys (name, shares, price) '''
  portfolio = []

  with open(filename, 'rt') as file:
    rows = csv.reader(file)
    headers = next(rows)

    for row in rows:
      try:
        record = dict(zip(headers, row))
        stock = {
          'name': record['name'],
          'shares': int(record['shares']),
          'price': float(record['price'])
        }
        portfolio.append(stock)
      except ValueError:
        print('Error: There was a problem with the data format in the file.')
        continue
  return portfolio

def read_prices(filename):
  '''
  Read a CSV file of price data into a dict mapping names to prices.
  '''
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


def make_report(portfolio, prices):
  '''
  Make a list of (name, shares, price, change) tuples given a portfolio list and a price dict.
  '''
  rows = []

  for stock in portfolio:
    current_price = prices.get(stock['name'], 0)
    change = current_price - stock['price']
    rows.append((stock['name'], stock['shares'], current_price, change))

  return rows

def print_report(reportdata):
  '''
  Print a nicely formatted report of (name, shares, price, change) tuples.
  '''
  headers = ('Name', 'Shares', 'Price', 'Change')
  print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
  print(f'{"-"*10} {"-"*10} {"-"*10} {"-"*10}')
  for row in reportdata:
    print(f'{row[0]:>10s} {row[1]:>10d} {row[2]:>10.2f} {row[3]:>10.2f}')

def portfolio_report(portfolio_file, prices_file):
  '''
  Make a stock report from a portfolio file and a prices file.
  '''

  # Read data file
  portfolio = read_portfolio(portfolio_file)
  prices = read_prices(prices_file)

  # Create the report data
  report = make_report(portfolio, prices)

  # Print it out
  print_report(report)

# Uncomment the following line to run the program
portfolio_report('Data/portfolio.csv', 'Data/prices.csv')