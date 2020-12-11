import itertools as it

with open('day10.txt', 'r') as f:
    puzzle_input = f.read().splitlines()

adapter_input = list(map(int, puzzle_input))

sorted_adapter_input = sorted(adapter_input)
outlet = 0
built_in_adapter = sorted_adapter_input[-1] + 3

"""
one_jolt_differences = 1
three_jolt_differences = 1

i = 1
while i < len(sorted_adapter_input):
    diff = sorted_adapter_input[i] - sorted_adapter_input[i-1]
    if diff == 1:
        one_jolt_differences += 1
    elif diff == 3:
        three_jolt_differences += 1
    else:
        print('Neither three nor one jolt difference.')
    i += 1

print(one_jolt_differences * three_jolt_differences)
"""


def findValidArrangement2(input_list: list):
    i = 1
    while i < len(input_list):
        diff = input_list[i] - input_list[i - 1]
        if diff <= 3:
            pass
        else:
            return False
        i += 1
    return True


def findValidArrangement(input_list: list):
    return input_list[-1] - input_list[-2] <= 3


print(sorted_adapter_input)

cannot_change = []
for num in sorted_adapter_input:
    num_index = sorted_adapter_input.index(num)
    if num_index < len(sorted_adapter_input) - 1 and sorted_adapter_input[num_index+1] - num == 3:
        if num not in cannot_change:
            cannot_change.append(num)
        if sorted_adapter_input[num_index+1] not in cannot_change:
            cannot_change.append(sorted_adapter_input[num_index+1])
cannot_change.append(165)
combos = []
i = 0
while i < len(cannot_change) - 1:
    from_value = cannot_change[i]
    to_value = cannot_change[i + 1]
    sorted_index_from = sorted_adapter_input.index(from_value) + 1
    sorted_index_to = sorted_adapter_input.index(to_value)
    if len(sorted_adapter_input[sorted_index_from:sorted_index_to]) > 0:
        combos.append(sorted_adapter_input[sorted_index_from:sorted_index_to])
    i += 1

combo_values = [2]
for combo in combos:
    value = 1
    j = 1
    while j < len(combo):
        value += len(list(it.combinations(combo, j)))
        j += 1
    if sorted_adapter_input[sorted_adapter_input.index(combo[-1])+1] - sorted_adapter_input[sorted_adapter_input.index(combo[0])-1] <= 3:
        value += 1
    combo_values.append(value)

ans = 1
for n in combo_values:
    ans *= n
print(ans)
