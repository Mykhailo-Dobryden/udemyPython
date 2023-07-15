def dict_to_list(dicts):
    new_list = []
    for k, v in dicts.items():
        if type(v) == int:
            v *= 2
        new_list.append((k, v))
    print(new_list)


dict_to_list({'brand': 'BMW', 'price': 100000, 'gearbox': "Automat", 'owner': 5})
dict_to_list({'a': 5, 'b': [], 'c': 100})
