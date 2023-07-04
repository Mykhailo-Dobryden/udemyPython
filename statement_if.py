# def nums_info(a, b):
#     if (type(a) is not int) or (type(b) is not int):
#         return "One of the arguments isn't int"
#
#     if a >= b:
#         return f"{a} greater than or equal {b}"
#
#     return f"{a} less than {b}"


def nums_info(a, b):
    if (type(a) is not int) or (type(b) is not int):
        info = "One of the arguments isn't int"
    elif a >= b:
        info = f"{a} greater than or equal {b}"
    else:
        info = f"{a} less than {b}"
    return info


print(nums_info(True, 10))

print(nums_info(10, 2))
print(nums_info(4, 15))
