import re
from itertools import product

with open('day14.txt', 'r') as f:
    puzzle_input = f.read().splitlines()

bitmask = ''
memory = {}  # { address: value }

line_re = r'([a-z0-9\[\]]+) = ([X0-9]+)'


def changeMask(mask: str):
    global bitmask
    bitmask = mask


"""
def applyMask(value: int):
    global bitmask
    bitmask = list(bitmask)
    binary_value = str(bin(value))[2:]
    additional_zeroes = (36 - len(binary_value)) * '0'
    bit_36_value = list(additional_zeroes + binary_value)

    for i in range(len(bit_36_value)):
        if bitmask[i] == 'X':
            pass
        else:  # bitmask[i] == '1' or '0'
            bit_36_value[i] = bitmask[i]

    bitmask = "".join(bitmask)
    bit_36_value = "".join(bit_36_value)
    return bit_36_value


for line in puzzle_input:
    init_line = re.findall(line_re, line)[0]
    instruction = init_line[0]
    value = init_line[1]
    if instruction == 'mask':
        changeMask(value)
    else:
        mem_line = re.findall(r'([0-9]+)', instruction)[0]
        memory[mem_line] = applyMask(int(value))

sum = 0
for item in memory.items():
    sum += int(item[1], 2)

print(sum)
"""

# Part 2


def findAddresses(input_addess: int):
    global bitmask
    address_binary_value = str(bin(input_addess))[2:]
    additional_zeroes = (36 - len(address_binary_value)) * '0'
    bit_36_address = list(additional_zeroes + address_binary_value)
    mask = list(bitmask)
    number_of_floating_values = mask.count('X')

    # Changes the address to overwrite 1s and include floating bits
    for i in range(len(bit_36_address)):
        if mask[i] == '1' or mask[i] == 'X':
            bit_36_address[i] = mask[i]
        else:
            pass

    possible_combinations_for_floating = list(product(
        [0, 1], repeat=number_of_floating_values))

    all_addresses = list()

    for c in possible_combinations_for_floating:
        j = 0
        working_address = bit_36_address.copy()
        for i in range(len(bit_36_address)):
            if bit_36_address[i] == 'X':
                working_address[i] = str(c[j])
                j += 1
            else:
                pass
        str_address = "".join(working_address)
        int_address = int(str_address, 2)
        all_addresses.append(int_address)

    return all_addresses


for line in puzzle_input:
    init_line = re.findall(line_re, line)[0]
    instruction = init_line[0]
    value = init_line[1]
    if instruction == 'mask':
        changeMask(value)
    else:
        address_value = int(re.findall(r'([0-9]+)', instruction)[0])
        new_addresses = findAddresses(address_value)
        for a in new_addresses:
            memory[a] = int(value)

sum = 0
for i in memory.items():
    sum += i[1]

print(sum)
