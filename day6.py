with open('day6.txt', 'r') as f:
    groups = f.read().split('\n\n')

group_answers = []

for group in groups:
    people = group.splitlines()  # To remove '\n'
    people = "".join(people)
    group_answers.append(people)

reduced_answers = []

for group in group_answers:
    reduced_answers.append("".join(set(group)))


sum_of_answers = 0
for group in reduced_answers:
    sum_of_answers += len(group)

# print(sum_of_answers) # part one answer


# Part 2
group_answers_part_2 = []
for group in groups:
    people = group.splitlines()
    group_answers_part_2.append(people)

reduced_answers_part_2 = []

for group in group_answers_part_2:
    num_of_groups = len(group)
    if num_of_groups == 1:
        reduced_answers_part_2.append(group[0])
    else:
        reduced_answers_part_2.append(set(group[0]).intersection(*group))


sum_of_answers_part_2 = 0
for ans in reduced_answers_part_2:
    if ans == set():
        pass
    else:
        sum_of_answers_part_2 += len(ans)

print(sum_of_answers_part_2)
