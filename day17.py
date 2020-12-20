
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

print(initial_state)
