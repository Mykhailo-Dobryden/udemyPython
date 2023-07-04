def merge_lists_to_dict(list_one, list_two):
    list_dict = dict(zip(list_one, list_two))
    return list_dict



list_of_iphone_with_price = merge_lists_to_dict(
    list_one = ['iphone11', 'iphone12', 'iphone13'], 
    list_two = [340, 450, 500])
print(list_of_iphone_with_price)


res2 = merge_lists_to_dict(
    ['a', 'b', 'c', 'd',], list_two= [45, 66, 77, 88]
)
print(res2)


