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


# def filter_list(list_to_filter, value_type):
#     return list(filter(lambda elem: type(elem) is value_type, list_to_filter))
#
#
# print(filter_list([1, 10, True, 'abc', 5.5], int))
# print(filter_list([1, 10, True, 'abc', 5.5], str))
# print(filter_list([1, 10, True, 'abc', 5.5], float))