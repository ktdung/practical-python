prices = {}

with open("Data/prices.csv") as f:
  for line in f:
    if len(line.strip()) == 0:
      continue
    row = line.split(',')
    prices[row[0].strip().strip('"')] = float(row[1])


print(prices)