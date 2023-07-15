# 1. Создайте список из 5 элементов разных типов
my_list = ['Fora', 25, True, 0.89, ['hkjhhj'] ]
print(my_list)

# 2. Удалите третий элемент

my_list.pop(2)
print(my_list)

# 3. Вывидите в терминал длину списка

print(len(my_list))

# 4. Поменяйте порядок следования элементов в списке

# my_list[0], my_list[1], my_list[2], my_list[3] = my_list[3], my_list[2], my_list[1], my_list[0]

my_list.reverse()
print(my_list)

# 5.  Создайте еще один список с двумя элементами

new_list = [False, 58]

# 6. Расширьте первый список элементами второго списка

# my_list += new_list

my_list.extend(new_list)


# 7. Вывидите в терминал расширенный список из 6 элементов

print(my_list)