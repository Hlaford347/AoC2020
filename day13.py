from functools import reduce
import math
from operator import itemgetter, mul
with open('day13.txt', 'r') as f:
    puzzle_input = f.read().splitlines()

timestamp = int(puzzle_input[0])

buses = list(puzzle_input[1].split(","))

running_buses = []
"""
for bus in buses:
    if bus != 'x':
        running_buses.append(int(bus))

next_times = []

for bus in running_buses:
    next_times.append([bus, math.ceil(timestamp/bus) * bus])

next_bus_list = sorted(next_times, key=itemgetter(1))

# Part 1
# print(next_bus_list[0][0] * (next_bus_list[0][1] - timestamp))
"""
multiple = 1
for bus in buses:
    if bus != 'x':
        running_buses.append(int(bus))
        multiple *= int(bus)
    else:
        running_buses.append('x')

bus_departure = []
for i in range(len(running_buses)):
    bus_departure.append([i, running_buses[i]])


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


"""
if __name__ == '__main__':
    n = [67, 7, 59, 61]
    a = [0, 6, 57, 58]
    print(chinese_remainder(n, a))
"""

a = []
n = []

for bus in bus_departure:
    if bus[1] != 'x':
        a.append(bus[1]-bus[0])
        n.append(bus[1])

print(chinese_remainder(n, a))
