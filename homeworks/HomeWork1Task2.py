list_fruits = ['banana', 'apple', 'pineapple', 'peach', 'plum']

list_vegetables = ['tomatos', 'potatos', 'cucumber', 'onion', 'cabbage']

united_lists = list_fruits + list_vegetables

print('Unite list with +: ', united_lists)
print('       ')
print('United list with magic method .__add__: ' , list_fruits.__add__(list_vegetables))

