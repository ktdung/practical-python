# report.py
#
# Exercise 2.4: A list of tuples
# Exercise 2.5: List of Dictionaries
# Exercise 2.7: Finding out if you can retire


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

def make_report():
  portfolio = read_portfolio('Data/portfolio.csv')
  prices = read_prices('Data/prices.csv')

  total_code = 0.0
  current_value = 0.0

  for stock in portfolio:
    cost = stock['shares'] * stock['price']
    total_code += cost
    current_price = prices.get(stock['name'], 0)
    current_value += stock['shares'] * current_price

  print(f'Total cost of portfolio: ${total_code:,.2f}')
  print(f'Current value of portfolio: ${current_value:,.2f}')

  gain_loss = current_value - total_code
  if gain_loss > 0:
    print(f'You have a gain of: ${gain_loss:,.2f}')
  elif gain_loss < 0:
    print(f'You have a loss of: ${-gain_loss:,.2f}')
  else:
    print('You have neither a gain nor a loss.')
def main():
  make_report()

main()