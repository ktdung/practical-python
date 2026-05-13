import fileparse
import sys

def read_portfolio(filename):
    '''
    Reads a portfolio file and returns a list of dictionaries
    with keys (name, shares, price)
    '''
    with open(filename, 'rt') as lines:
        return fileparse.parse_csv(lines, select=['name', 'shares', 'price'], types=[str, int, float])

def read_prices(filename):
  '''
  Read a CSV file of price data into a dict mapping names to prices.
  '''
  with open(filename, 'rt') as lines:
      return dict(fileparse.parse_csv(lines, types=[str, float], has_headers=False))


def make_report_data(portfolio, prices):
  '''
  Make a list of (name, shares, price, change) tuples given a portfolio list and a price dict.
  '''
  rows = []

  for stock in portfolio:
    current_price = prices[stock['name']]
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
  report = make_report_data(portfolio, prices)

  # Print it out
  print_report(report)

# Uncomment the following line to run the program

def main(args):
    print(args)
    if len(args)  != 3:
        raise SystemExit(f'Usage: {args[0]} portfolio-file prices-file')
    portfolio_report(args[1], args[2])



if __name__ == '__main__':
  import sys
  main(sys.argv)