import fileparse
import sys
import stock
import tableformat

def read_portfolio(filename):
    '''
    Reads a portfolio file and returns a list of dictionaries
    with keys (name, shares, price)
    '''
    with open(filename, 'rt') as lines:
        portdicts =  fileparse.parse_csv(lines, select=['name', 'shares', 'price'], types=[str, int, float])
        portfolio = [stock.Stock(d['name'], d['shares'], d['price']) for d in portdicts]
    return portfolio

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

  for s in portfolio:
    current_price = prices[s.name]
    change = current_price - s.price
    rows.append((s.name, s.shares, current_price, change))
  return rows

def print_report(reportdata, formatter):
  '''
  Print a nicely formatted report of (name, shares, price, change) tuples.
  '''
  formatter.headings(["Name", "Shares", "Price", "Change"])
#   print(f'{"-"*10} {"-"*10} {"-"*10} {"-"*10}')
  for row in reportdata:
    rowdata = [row[0], str(row[1]), f'{row[2]:.2f}', f'{row[3]:.2f}']
    formatter.row(rowdata)

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
  formatter = tableformat.CSVTableFormatter()
  print_report(report, formatter)

# Uncomment the following line to run the program

def main(args):
    print(args)
    if len(args)  != 3:
        raise SystemExit(f'Usage: {args[0]} portfolio-file prices-file')
    portfolio_report(args[1], args[2])



if __name__ == '__main__':
  import sys
  main(sys.argv)