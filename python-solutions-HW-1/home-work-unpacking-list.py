user_info_list = [
    {'name': 'Dasha', 'age': 35},
    {'name': 'Misha', 'age': 18},
    {'name': 'Tanya', 'age': 25}
]


def get_user_info(name, age):
    return f"{name} is {age} years old"


user_1, user_2, user_3 = user_info_list

print(get_user_info(**user_1))
print(get_user_info(**user_2))
print(get_user_info(**user_3))
