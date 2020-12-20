import re
with open('day16.txt', 'r') as f:
    puzzle_input = f.read().splitlines()

tickets = []

for line in puzzle_input:
    tickets.append(line.split(","))

rules = tickets[0:20]

my_ticket = tickets[22]

nearby_tickets = tickets[25:]

# something like this?
# rules list [{"rule1": [x-y],
#               "valid": boolean},
#             {"rule2": [x-y],
#               "valid": boolean}]
# for rule in rules:
# validate?

rule_dict = {}


def createRuleset():
    global rules
    global rule_dict
    re_rule_range = r'([0-9]+-[0-9]+) or ([0-9]+-[0-9]+)'
    re_rule_name = r'([\w\s]+):'
    re_range_value = r'([0-9]+)-([0-9]+)'
    rules_ranges = list()
    for rule in rules:
        ranges = re.findall(re_rule_range, rule[0])[0]
        rule_name = re.findall(re_rule_name, rule[0])[0]
        range_one = ranges[0]  # '37-479'
        range_two = ranges[1]  # '485-954'
        first_range = re.findall(re_range_value, range_one)[0]
        second_range = re.findall(re_range_value, range_two)[0]
        complete_range = list(range(int(first_range[0]), int(
            first_range[1]) + 1)) + list(range(int(second_range[0]), int(second_range[1]) + 1))
        rules_ranges.append(complete_range)
        rule_dict[rule_name] = complete_range

    return rules_ranges


rules_range = createRuleset()
invalid_values = list()
valid_tickets = list(nearby_tickets)  # Used for part 2
for t in nearby_tickets:
    for n in t:
        n = int(n)
        valid = False
        for rule in rule_dict.items():
            if n in rule[1]:
                valid = True

        if not valid:
            invalid_values.append(n)
            valid_tickets.remove(t)

# print(sum(invalid_values))

valid_rules = list()

for rule in rule_dict.items():
    for col in range(len(rule_dict.items())):
        valid = True
        for t in valid_tickets:
            t_num = int(t[col])
            if t_num not in rule[1]:
                valid = False

        if valid:
            valid_rules.append([rule[0], col])

for rule in valid_rules:
    print(rule)

# Did this part in excel

departure_rows = [0, 4, 7, 10, 16, 17]

multiple = 1

for row in departure_rows:
    multiple *= int(my_ticket[row])

print(multiple)
