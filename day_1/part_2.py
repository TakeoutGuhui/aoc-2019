from math import floor

def calculate_fuel(mass):
    fuel = floor(mass / 3) - 2
    if fuel <= 0:
        return 0
    return fuel + calculate_fuel(fuel)

with open('input.txt') as f:
    lines = f.readlines()

result = sum([calculate_fuel(float(line)) for line in lines])

print(result)