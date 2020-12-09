import re

with open('day7.txt', 'r') as f:
    rules = f.read().splitlines()

re_bags = r'([\w]+ [\w]+) bags contain ([\w?\d?\s?,?]+)[.]'

possible_bags = 0

rules_list = []  # separated rules

for rule in rules:
    rules_list.append(re.findall(re_bags, rule))


initial_bag = 'shiny gold'

containing_bags = []

parents = []
"""
for rule in rules_list:
    obj = {'color': rule[0][0], 'contains': rule[0][1]}
    containing_bags.append(obj)

for bag in containing_bags:
    if 'shiny gold' in bag['contains']:
        parents.append(bag['color'])

for bag in containing_bags:
    for parent in parents:
        if parent in bag['contains']:
            if bag['color'] not in parents:
                parents.append(bag['color'])
running = True
while running:
    starting_length = len(parents)
    for bag in containing_bags:
        for parent in parents:
            if parent in bag['contains']:
                if bag['color'] not in parents:
                    parents.append(bag['color'])
    ending_length = len(parents)
    if starting_length == ending_length:
        running = False

print(len(parents))
"""
"""
rules_list = [[('shiny gold', '2 dark red bags.')],
              [('dark red', '2 dark orange bags.')],
              [('dark orange', '2 dark yellow bags.')],
              [('dark yellow', '2 dark green bags.')],
              [('dark green', '2 dark blue bags.')],
              [('dark blue', '2 dark violet bags.')],
              [('dark violet', 'no other bags.')]]

rules_list = [[('light red', '1 bright white bag, 2 muted yellow bags.')],
              [('dark orange', '3 bright white bags, 4 muted yellow bags.')],
              [('bright white', '1 shiny gold bag.')],
              [('muted yellow', '2 shiny gold bags, 9 faded blue bags.')],
              [('shiny gold', '1 dark olive bag, 2 vibrant plum bags.')],
              [('dark olive', '3 faded blue bags, 4 dotted black bags.')],
              [('vibrant plum', '5 faded blue bags, 6 dotted black bags.')],
              [('faded blue', 'no other bags.')],
              [('dotted black', 'no other bags.')]]
"""
containing_bags = {}

for rule in rules_list:
    containing_bags[rule[0][0]] = rule[0][1]

re_contains = r'([0-9]+) ([\w\s]+) bag'

# find why answer is 127 not 126


def findChildren(color):
    # separating children and counts into groups
    children = re.findall(re_contains, containing_bags.get(color))

    sum_of_bags = 0

    for child in children:
        count = int(child[0])
        next_color = child[1]
        sum_of_bags += count * findChildren(next_color)
    if len(children) > 0:
        return sum_of_bags + 1
    else:
        return 1


print(findChildren('shiny gold') - 1)
