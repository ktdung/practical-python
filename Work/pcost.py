import sys
import report
def portfolio_cost(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    portfolio = report.read_portfolio(filename)
    return sum(stock.cost for stock in portfolio)


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

