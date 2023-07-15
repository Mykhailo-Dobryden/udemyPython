def merge_lists_to_dict(list_one, list_two):
    list_dict = dict(zip(list_one, list_two))
    return list_dict


list_iPhone = ['iPhone 11', 'iPhone 12', 'iPhone 13', 'iPhone 14']
list_price = [500, 600, 700, 100]

price_of_iPhones = merge_lists_to_dict(list_iPhone, list_price)
print(price_of_iPhones)

res_one = merge_lists_to_dict(['a', 'b', 'c', 'd'], [0.4, True, (45, -8), 'abvgdaika'])
print(res_one)
