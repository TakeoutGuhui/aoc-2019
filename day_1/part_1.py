from math import floor

with open('input.txt') as f:
    lines = f.readlines()

result = sum([floor(float(line) / 3) - 2 for line in lines])

print(result)