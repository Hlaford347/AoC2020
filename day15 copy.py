from operator import itemgetter
import operator
input = [8, 11, 0, 19, 1, 2]  # 0 4 0 2 4 3 0
nums = {}
i = 1
for item in input:
    nums[item] = i
    i += 1

print(nums)

next_number = 0

while i < 30000001:

    current_number = next_number
    if next_number in nums.keys():
        next_number = i - nums.get(next_number)
    else:
        next_number = 0
    nums[current_number] = i
    i += 1
"""
while i < 30000000:
    last_spoken_number = input[-1]
    if last_spoken_number in input[:-1]:
        # inverted_list = input[-2::-1]
        # last_time_spoken = inverted_list.index(last_spoken_number)
        next_number = len(input) - input.index(last_spoken_number) - 1
        input.remove(last_spoken_number)
    else:
        next_number = 0
    input.append(next_number)
    i += 1
"""
print(max(nums.items(), key=itemgetter(1))[0])
