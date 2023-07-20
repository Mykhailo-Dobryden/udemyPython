"""1. Создайте цикл, в которм нужно попросить пользователя
ввести в терминале два числаю
2. Выведите в терминал результат деления первого числа на второе.
3. После этого спросите пользователя, хочет ли он продолжать yes/no.
4. Усли ответ ноу, то нужно выйти из цикла.
5. Иначе нужно повторить все сначала.
"""
#
# while True:
#     number_1 = float(input("Enter first number: "))
#     number_2 = float(input("Enter second number: "))
#     print(f"the result of division {number_1 / number_2}")
#     answer = input("Do you want to continue? yes/no: ")
#     if answer == 'yes':
#         continue
#     break


while True:
    try:
        num_one = float(input("Enter number one: "))
        num_two = float(input("Enter number two: "))
    except ValueError as e:
        print(e)
        print("You must enter numbers!")
        continue

    print(num_one / num_two)

    answer = input("Do you want to continue? (yes/no): ")
    if answer == 'no':
        break
