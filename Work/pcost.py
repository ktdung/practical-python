# pcost.py
#
# Exercise 1.27
with open("Data/portfolio.csv", 'rt') as file:
  total_cost = 0.0
  next(file)
  for line in file:
    parts = line.split(',')
    shares = int(parts[1])
    price = float(parts[2])
    total_cost += shares * price
  print(f'Total cost: {total_cost}')