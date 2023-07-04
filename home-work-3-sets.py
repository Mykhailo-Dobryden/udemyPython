nums = {5, 8, 15, 67, 35}

nums.add(13)

print(nums)

other_nums = {5, 8, 11, 42, 35}

print(nums.intersection(other_nums))
common_nums = nums.intersection(other_nums)

print(common_nums)

list_common_nums = list(common_nums)

print(list_common_nums)

