import re
with open('day18.txt', 'r') as f:
    puzzle_input = f.read().splitlines()

# make it a list of numbers and symbolthingies
# look for parentheses, then whatever is between parentheses, read and calculate first
# then go from left to right through the list? Is that doable?
# so if 9 * 8 + 2 + (4 * (2 * 2 + 9 * 2) * 9 * 3 * 8) + 8 * 5

re_parenthesis = r'(\([\d\s\*\+]+\))'
re_numbers = r'([0-9]+)'
re_operator = r'[\*|\+]'
re_addition = r'([0-9]+)([\+])([0-9]+)'
re_multiplication = r'([0-9]+)([\*])([0-9]+)'


def solver(equation: str):
    if equation[0] == '(':
        stripped_operation = equation[1:-1]
    else:
        stripped_operation = equation

    reduced_string = stripped_operation.replace(" ", "")

    while len(re.findall(re_addition, reduced_string)) > 0:
        first = int(re.findall(re_addition, reduced_string)[0][0])
        second = int(re.findall(re_addition, reduced_string)[0][2])
        op = re.findall(re_addition, reduced_string)[0][1]
        substring = str(first) + str(op) + str(second)
        value = first + second

        reduced_string = reduced_string.replace(
            substring, str(value), 1)

    while len(re.findall(re_multiplication, reduced_string)) > 0:
        first = int(re.findall(re_multiplication, reduced_string)[0][0])
        second = int(re.findall(re_multiplication, reduced_string)[0][2])
        op = re.findall(re_multiplication, reduced_string)[0][1]
        substring = str(first) + str(op) + str(second)
        value = first * second

        reduced_string = reduced_string.replace(
            substring, str(value), 1)
    """
    Part 1
    while len(re.findall(re_operator, reduced_string)) > 0:
        numbers = re.findall(re_numbers, reduced_string)
        first = int(numbers[0])
        second = int(numbers[1])
        op = re.findall(re_operator, reduced_string)[0]
        substring = str(first) + str(op) + str(second)
        value = 0

        if op == '*':
            value = first * second
        elif op == '+':
            value = first + second
        else:
            print('Error')

        reduced_string = reduced_string.replace(
            substring, str(value), 1)
    """
    return str(reduced_string)


sums = 0
sum_list = []

for line in puzzle_input:
    remaining_parenthesis = True
    working_line = line
    while remaining_parenthesis:
        inner_parenthesis = re.findall(re_parenthesis, working_line)

        if len(inner_parenthesis) > 0:
            for para in inner_parenthesis:
                subanswer = solver(para)
                substring = str(para)
                working_line = working_line.replace(substring, subanswer)

        else:
            remaining_parenthesis = False

    sum_list.append(int(solver(working_line)))
    sums += int(solver(working_line))

print(sums)
