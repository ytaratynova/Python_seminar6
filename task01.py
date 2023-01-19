# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# number = input("Введите число: ")
# sum = 0
# for i in range(len(number)):
#     if number[i].isdigit():
#         sum += int(number[i])
# print(f'Сумма цифр числа {number} = {sum}')

number = input("Введите число: ")
sum_number = sum([int(i) for i in number if i.isdigit()])
print(f'Сумма цифр числа {number} = {sum_number}')

