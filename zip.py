# fruits = ['apple', 'banana', 'lime', 'orange']
# quantities = '3456'

# fruit_qtys_zip = zip(fruits, quantities)
# print(fruit_qtys_zip)
# fruit_qtys_list = dict(fruit_qtys_zip)
# print(fruit_qtys_list)

goods = ['TV', 'Laptop', 'Phone', 'Tablet']
price = (1200, 500, 375, 680)

goods_with_price_zip = zip(goods, price)
# goods_with_price_zip = print(dict(list(zip(goods, price))))
goods_with_price_list = list(goods_with_price_zip)
print(goods_with_price_list)
goods_with_price_dict = dict(goods_with_price_list)
print(goods_with_price_dict)