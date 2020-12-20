from operator import itemgetter

input = [8, 11, 0, 19, 1, 2]  # 0 4 0 2 4 3 0
nums = {}
i = 1
for item in input:
    nums[item] = i
    i += 1

next_number = 0

while i < 30000001:

    current_number = next_number
    if next_number in nums.keys():
        next_number = i - nums.get(next_number)
    else:
        next_number = 0
    nums[current_number] = i
    i += 1
print(max(nums.items(), key=itemgetter(1))[0])
