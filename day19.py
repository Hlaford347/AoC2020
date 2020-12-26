import re
with open('day19.txt', 'r') as f:
    puzzle_input = f.read().splitlines()

rules = dict()
re_rule = r'([0-9]+): ("[\w]+"|[\d ]+ ?[\|\d ]+)'
re_numbers = r'([0-9]+)'

for line in puzzle_input:
    rule = re.findall(re_rule, line)
    if len(rule) > 0:
        r = rule[0][0]
        rules[r] = rule[0][1]

while len(re.findall(re_numbers, rules.get('0'))) > 0:
    rule_zero_rule = rules.get('0')
    working_rule = re.findall(re_numbers, rules.get('0'))[0]
    new_rule = rule_zero_rule.replace(
        working_rule, rules.get(working_rule))
    rules['0'] = new_rule

print(rules['0'])
