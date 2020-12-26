
with open('day20.txt', 'r') as f:
    puzzle_input = f.read()
    puzzle_input = puzzle_input.split("\n\n")
    initial_input = []
    for g in puzzle_input:
        initial_input.append([item.strip() for item in g.split('\n')])

initial_input = initial_input[:-1]
tiles_dict = {}

for tile in initial_input:
    name = tile[0][:-1]
    top = tile[1]
    bottom = tile[-1]

    left = ''
    right = ''
    for row in tile[1:]:
        left += row[0]
        right += row[-1]

    tiles_dict[name] = [top, bottom, left, right,
                        top[::-1], bottom[::-1], left[::-1], right[::-1]]

corners = []

for tile in tiles_dict.items():
    sides = tile[1]
    matches = 0
    for side in sides:
        for value in tiles_dict.values():
            if side in value:
                matches += 1

    if matches <= 12:
        corners.append(tile)

print(corners)
