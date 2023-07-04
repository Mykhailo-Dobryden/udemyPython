dict_one = {
    'brand': "BMW",
    'speed': 200,
    'price': 50_000,
    'availability': True
}

dict_two = {
    'availability': True,
    'brand': "BMW",
    'speed': 200,
    'price': 50_000
}

dict_one == dict_two and print("Dictionaries are equal")
