with open('day1.txt', 'r') as f:
    list_of_str = f.read().splitlines()

p_int = list(map(lambda x: int(x), list_of_str))

# a + b = 2020
# 2020 - a = b, search list for b

sum = []

"""
for a in p_int:
    b = 2020 - a
    if b in p_int:
        sum.append((a, b))
"""

# part 1 answer
# print(pairs[0][0] * pairs[0][1])

p_int = sorted(p_int)

for a in p_int:
    for b in p_int:
        if a + b > 2020:
            break
        else:
            c = 2020 - a - b
            if c in p_int:
                sum.append((a, b, c))

# part 2 answer
print(sum[0][0] * sum[0][1] * sum[0][2])
