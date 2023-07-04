# def mult(a, b):
#     return a * b


# def mult(a, b): return a * b


# print(mult(10, 5))


def greeting(greet):
    return lambda name: f"{greet}, {name}"

# def greeting(greet):
#     def info(name):
#         return f"{greet}, {name}"
#     return info


morning_greeting = greeting('Good Morning')
print(morning_greeting('Misha'))

evening_greeting = greeting("Good Evening")
print(evening_greeting('Mykhailo'))
