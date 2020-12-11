with open('day9.txt', 'r') as f:
    puzzle_input = f.read().splitlines()

preamble_pre = puzzle_input[:25]
preamble = []

preamble = list(map(int, preamble_pre))

puzzle_input_pre = puzzle_input[25:]
puzzle_input = []

puzzle_input = list(map(int, puzzle_input_pre))

index = 0
valid_number = True
invalid_number = 0  # Answer in part 1

while valid_number:
    number = puzzle_input[index]
    for n in preamble:
        if number - n in preamble and number - n is not n:
            preamble.pop(0)
            preamble.append(number)
            break
        elif preamble.index(n) == len(preamble)-1:
            invalid_number = number
            valid_number = False
            break
        else:
            pass

    index += 1

index_from = 0
index_to = 2

searching = True

while searching:
    temp_sum = sum(puzzle_input[index_from:index_to])
    if temp_sum < invalid_number:
        index_to += 1
    elif temp_sum == invalid_number:
        searching = False
        print(sorted(puzzle_input[index_from:index_to]), sorted(
            puzzle_input[index_from:index_to])[0] + sorted(puzzle_input[index_from:index_to])[-1])
    elif temp_sum > invalid_number:
        index_from += 1
        index_to = index_from + 2
