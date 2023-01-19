# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

# number = int(input("Введите натуральное число: "))
# list_of_lists = []
# sum = 0
# for i in range(1, number + 1):
#     list_of_lists.append([i, round(((1 + 1/i)**i),2)])
#     sum += round((1 + 1/i)**i, 2)
# print(list_of_lists)
# print(f'Сумма чисел последовательности (1 + 1/n)^n: {sum}')

number = int(input("Введите натуральное число: "))
sum_my_list = sum([round(((1 + 1/i)**i),2) for i in range(1, number + 1)])
print(f'Сумма чисел последовательности (1 + 1/n)^n: {sum_my_list}')

