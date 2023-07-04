def filter_list(list_object, type_info):
    new_list = []
    for elem in list_object:
        if type(elem) == type_info:
            new_list.append(elem)
            # print(new_list)
    return new_list


print(filter_list([35, True, 'abc', 10], int))
print(filter_list([35, True, 'abc', 10], str))
print(filter_list([35, True, 'abc', 10], bool))
