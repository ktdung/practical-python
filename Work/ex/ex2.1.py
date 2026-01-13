# 2.1 Tuple
import csv

f= open('../Data/portfolio.csv', 'r')
rows = csv.reader(f)

row1 = next(rows)
print(row1)
row2 = next(rows)
t = (row2[0], int(row2[1]), float(row2[2]))
print(f"{t[1] * t[2]:0.2f}")