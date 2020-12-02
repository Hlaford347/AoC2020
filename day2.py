import re

with open('day2.txt', 'r') as f:
    pwds = f.read().splitlines()

policies = []

re_pattern = "([\d]+)-([\d]+) ([\w]): ([\w]+)"

for line in pwds:
    policy = re.findall(re_pattern, line)

    policies.append(policy)

valid_pwds = []

""" Part 1 solution
def check_policy(policy: tuple):
    min_num = int(policy[0])
    max_num = int(policy[1])
    character = policy[2]
    password = policy[3]

    if min_num <= password.count(character) and password.count(character) <= max_num:
        valid_pwds.append(password)
"""


def check_policy(policy: tuple):
    pos_a = int(policy[0]) - 1
    pos_b = int(policy[1]) - 1
    character = policy[2]
    password = policy[3]

    if (not password[pos_a] == character and password[pos_b] == character) or (password[pos_a] == character and not password[pos_b] == character):
        valid_pwds.append(password)


for policy in policies:
    check_policy(policy[0])

print(len(valid_pwds))
