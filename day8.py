import re
from copy import deepcopy

with open('day8.txt', 'r') as f:
    instructions = f.read().splitlines()

re_instructions = r'([a-z]{3}) ([+|-][0-9]+)'


initial_program = []

for line in instructions:
    initial_program.append(re.findall(re_instructions, line))

accumulator = 0
current_line = 0

visited_lines = []


def acc(value):
    global accumulator
    global current_line
    accumulator += value
    current_line += 1


def jmp(value):
    global current_line
    current_line += value


def nop():
    global current_line
    current_line += 1


running = True
while running:
    if current_line in visited_lines:
        running = False
    elif current_line > len(initial_program):
        running = False
        print(accumulator)
    else:
        current_instruction = initial_program[current_line][0]
        op = current_instruction[0]
        value = int(current_instruction[1])
        visited_lines.append(current_line)
        if op == 'acc':
            acc(value)
        elif op == 'jmp':
            jmp(value)
        elif op == 'nop':
            nop()
        else:
            print('error')


def runProgram(program):
    temp_visited_lines = []
    running = True
    global current_line
    current_line = 0
    while running:
        if current_line in temp_visited_lines:
            running = False
        elif current_line == len(program):
            running = False
            print(accumulator)
        else:
            current_instruction = program[current_line][0]
            op = current_instruction[0]
            value = int(current_instruction[1])
            temp_visited_lines.append(current_line)
            if op == 'acc':
                acc(value)
            elif op == 'jmp':
                jmp(value)
            elif op == 'nop':
                nop()
            else:
                print('error')


for line in visited_lines:
    accumulator = 0
    new_program = deepcopy(initial_program)
    current_instruction = new_program[line][0]
    if current_instruction[0] == 'jmp':
        new_program[line][0] = ('nop', new_program[line][0][1])
        runProgram(new_program)
    elif current_instruction[0] == 'nop':
        new_program[line][0] = ('jmp', new_program[line][0][1])
        runProgram(new_program)
    else:
        pass
