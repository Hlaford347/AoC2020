with open('day3.txt', 'r') as f:
    map = f.read().splitlines()

# open (.)
# tree (#)
# slope = right 3, down 1
starting_position = [0, 0]
current_position = starting_position

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]


def move(position, slope):
    global current_position
    x = position[0]
    y = position[1]

    x += slope[0]
    y += slope[1]
    current_position = [x, y]


trees = []
for slope in slopes:
    tree_count = 0
    while current_position[1] < len(map):
        move(current_position, slope)
        if current_position[1] < len(map) and map[current_position[1]][current_position[0] % len(map[current_position[1]])] == '#':
            print(current_position)
            tree_count += 1
    trees.append(tree_count)
    current_position = starting_position

product = 1
for count in trees:
    product *= count

print(trees, product)
