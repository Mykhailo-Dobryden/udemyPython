# a = 10

# def my_fn():
#     a = True
#     b = 15
#     print(a)
#     print(b)


# my_fn()

# print(a)
# print(b)
# ----------------------


a = 10


def my_fn():
    global a
    a = 15


my_fn()

print(a)
