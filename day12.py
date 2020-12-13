import math
with open('day12.txt', 'r') as f:
    puzzle_input = f.read().splitlines()

starting_position = [0, 0]
current_position = [0, 0]
waypoint_position = [10, 1]
facing_direction = 'E'

"""
def rotation(direction: str, degrees: int):
    global facing_direction
    compass = ['N', 'E', 'S', 'W']
    facing_index = compass.index(facing_direction)

    if direction == 'R':
        if degrees == 90:
            facing_direction = compass[(facing_index + 1) % len(compass)]
        if degrees == 180:
            facing_direction = compass[(facing_index + 2) % len(compass)]
        if degrees == 270:
            facing_direction = compass[(facing_index + 3) % len(compass)]
    if direction == 'L':
        if degrees == 90:
            facing_direction = compass[(facing_index - 1) % len(compass)]
        if degrees == 180:
            facing_direction = compass[(facing_index - 2) % len(compass)]
        if degrees == 270:
            facing_direction = compass[(facing_index - 3) % len(compass)]


def movement(direction: str, amount: int):
    global facing_direction
    global current_position
    if direction == 'F':
        direction = facing_direction

    if direction == 'N':
        current_position[1] += amount
    if direction == 'E':
        current_position[0] += amount
    if direction == 'S':
        current_position[1] -= amount
    if direction == 'W':
        current_position[0] -= amount

for line in puzzle_input:
    direction = line[0]
    amount = int(line[1:])

    if direction == 'R' or direction == 'L':
        rotation(direction, amount)
    elif direction == 'N' or direction == 'E' or direction == 'S' or direction == 'W' or direction == 'F':
        movement(direction, amount)
    else:
        print('Not R/L or N/E/S/W')
# Part 1
print(abs(current_position[0]) + abs(current_position[1]))

"""


def waypointMovement(direction: str, amount: int):
    global waypoint_position

    if direction == 'N':
        waypoint_position[1] += amount
    if direction == 'E':
        waypoint_position[0] += amount
    if direction == 'S':
        waypoint_position[1] -= amount
    if direction == 'W':
        waypoint_position[0] -= amount


def waypointRotation(direction: str, angle: int):
    global waypoint_position
    x = waypoint_position[0]
    y = waypoint_position[1]
    new_x = x
    new_y = y

    if direction == 'R':
        if angle == 90:
            new_x = y
            new_y = -x
        if angle == 180:
            new_x = -x
            new_y = -y
        if angle == 270:
            new_x = -y
            new_y = x
    if direction == 'L':
        if angle == 90:
            new_x = -y
            new_y = x
        if angle == 180:
            new_x = -x
            new_y = -y
        if angle == 270:
            new_x = y
            new_y = -x

    waypoint_position = [new_x, new_y]


def shipMovement(amount: int):
    global waypoint_position
    global current_position
    x = waypoint_position[0] * amount
    y = waypoint_position[1] * amount

    current_position[0] += x
    current_position[1] += y


for line in puzzle_input:
    direction = line[0]
    amount = int(line[1:])

    if direction == 'F':
        shipMovement(amount)
    elif direction == 'R' or direction == 'L':
        waypointRotation(direction, amount)
    else:  # N,E,S,W
        waypointMovement(direction, amount)

print(abs(current_position[0]) + abs(current_position[1]))
