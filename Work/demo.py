records = []

with open('Data/portfolio.csv', 'rt') as f:
  next(f) # skip header
  for line in f:
    row = line.split(',')
    records.append((row[0], int(row[1]), float(row[2]) ))

print(records)