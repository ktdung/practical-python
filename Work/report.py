# report.py
#
# Exercise 2.4: A list of tuples
# Exercise 2.5: List of Dictionaries
# Exercise 2.7: Finding out if you can retire
# Exercise 2.9: Collecting Data



import csv

def read_portfolio(filename):
  '''Reads a portfolio file and returns a list of (name, shares, price) tuples'''
  portfolio = []

  with open(filename, 'rt') as file:
    rows = csv.reader(file)
    next(rows)
    for row in rows:
      try:
        hoding = {
          'name': row[0],
          'shares': int(row[1]),
          'price': float(row[2])
        }
        portfolio.append(hoding)
      except ValueError:
        print('Error: There was a problem with the data format in the file.')
        continue
  return portfolio

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


def make_report(portfolio, prices):
  current_value = 0.0
  rows = []

  for stock in portfolio:
    current_price = prices.get(stock['name'], 0)
    change = current_price - stock['price']
    rows.append((stock['name'], stock['shares'], current_price, change))

  return rows

def main():
  portfolio = read_portfolio('Data/portfolio.csv')
  prices = read_prices('Data/prices.csv')
  report = make_report(portfolio, prices)

  headers = ('Name', 'Shares', 'Price', 'Change')
  print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
  print('---------- ---------- ---------- -----------')
  for r in report:
    name, shares, current_price, change = r
    print(f'{name:>10s} {shares:>10d} {current_price:>10.2f} {change:10.2f}')

main()