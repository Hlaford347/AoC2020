
with open('day17.txt', 'r') as f:
    puzzle_input = f.read().splitlines()


# '#' -active
# '.' -inactive
# 6 cycles

# If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise, the cube becomes inactive.
# If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive.

initial_state = list()

for line in puzzle_input:
    initial_state.append(list(line))

initial_dict = {}


z = 0
w = 0

for y in range(len(initial_state)):
    for x in range(len(initial_state[0])):
        initial_dict[(x, y, z, w)] = initial_state[y][x]


def getNeighbors(coords: tuple):
    range_x = (coords[0] - 1, coords[0] + 1)
    range_y = (coords[1] - 1, coords[1] + 1)
    range_z = (coords[2] - 1, coords[2] + 1)
    range_w = (coords[3] - 1, coords[3] + 1)

    neighbors = []

    # Gets all 26 neighbors
    for x in range(range_x[0], range_x[1]+1):
        for y in range(range_y[0], range_y[1]+1):
            for z in range(range_z[0], range_z[1]+1):
                for w in range(range_w[0], range_w[1]+1):
                    neighbors.append((x, y, z, w))

    neighbors.remove(coords)

    return neighbors


def getState(coords: tuple):
    global initial_dict
    return initial_dict.get(coords)


def setState(coords: tuple, current_state: str):
    global working_dict_copy
    neighbors = getNeighbors(coords)
    neighbors_active = 0

    for n in neighbors:
        if getState(n) == '#':
            neighbors_active += 1
        else:
            pass

    if current_state == '#' and neighbors_active < 2 or neighbors_active > 3:
        working_dict_copy[coords] = '.'
    elif current_state == '.' and neighbors_active == 3:
        working_dict_copy[coords] = '#'
    else:
        pass

# initial_dict is starting point
# working_dict_copy is the "active copy"


iteration = 0

while iteration < 6:
    working_dict_copy = initial_dict.copy()

    for cube in initial_dict.items():
        neighbors = getNeighbors(cube[0])
        for n in neighbors:
            if not getState(n):
                working_dict_copy[n] = '.'

    initial_dict = working_dict_copy.copy()
    for cube in initial_dict.items():
        coords = cube[0]
        state = cube[1]

        setState(coords, state)

    initial_dict = working_dict_copy.copy()
    iteration += 1

active_cubes = 0
for cube in initial_dict.items():
    if cube[1] == '#':
        active_cubes += 1

print(active_cubes)
