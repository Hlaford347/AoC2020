from copy import deepcopy

with open('day11.txt', 'r') as f:
    puzzle_input = f.read().splitlines()

"""
    If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
    Otherwise, the seat's state does not change.

    Seat_position[0] = X
    Seat_position[1] = Y
"""

puzzle_layout = []
for line in puzzle_input:
    puzzle_layout.append(list(line))

initial_layout = deepcopy(puzzle_layout)
working_copy = deepcopy(puzzle_layout)


def findSeat(direction: str, position: tuple):
    # position is (x,y) - (column,row)

    x = position[0]
    y = position[1]

    if direction == 'left':
        x -= 1

    if direction == 'left-up':
        x -= 1
        y -= 1

    if direction == 'up':
        y -= 1

    if direction == 'right-up':
        x += 1
        y -= 1

    if direction == 'right':
        x += 1

    if direction == 'right-down':
        x += 1
        y += 1

    if direction == 'down':
        y += 1

    if direction == 'left-down':
        x -= 1
        y += 1

    if x < 0 or y < 0 or x > len(initial_layout[0])-1 or y > len(initial_layout)-1:
        return '.'
    elif initial_layout[y][x] == '.':
        newTuple = (x, y)
        return findSeat(direction, newTuple)
    else:
        return initial_layout[y][x]


def changeSeat(seat_position: list):
    seat_state = initial_layout[seat_position[1]][seat_position[0]]

    seat_tuple = tuple(seat_position)
    directions = ['left', 'left-up', 'up', 'right-up',
                  'right', 'right-down', 'down', 'left-down']

    adjacent_seats = []

    for direction in directions:
        adjacent_seats.append(findSeat(direction, seat_tuple))

    if seat_state == 'L':
        if adjacent_seats.count('#') == 0:
            working_copy[seat_position[1]][seat_position[0]] = '#'
    elif seat_state == '#':
        if adjacent_seats.count('#') >= 5:
            working_copy[seat_position[1]][seat_position[0]] = 'L'
    else:
        working_copy[seat_position[1]][seat_position[0]
                                       ] = initial_layout[seat_position[1]][seat_position[0]]


running = True
while running:
    j = 0

    while j < len(initial_layout):
        i = 0

        while i < len(initial_layout[j]):
            changeSeat([i, j])
            i += 1
        j += 1

    if working_copy == initial_layout:
        running = False

    initial_layout = deepcopy(working_copy)

count = 0
for row in working_copy:
    count += row.count('#')

print(count)
