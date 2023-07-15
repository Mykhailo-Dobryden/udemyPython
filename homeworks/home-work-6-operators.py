set_one = {45, 64, 1, 4, 16, 20}
set_two = {64, 45, 1, 16, 4, 20}

print(id(set_one))
print(id(set_two))

print(set_one == set_two)
print(set_one.__eq__(set_two))

print(set_one is set_two)
print(45 in set_two)
