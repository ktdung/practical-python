# bounce.py
#
# Exercise 1.5
height = 100
bounce = 0.6
count = 0

while count < 10:
  count += 1
  height = height * bounce
  print(count, round(height, 4))