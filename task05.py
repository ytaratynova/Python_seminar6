# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и 
# минимальным значением дробной части элементов,
# отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# import random

# def FillTheList(length):
#     list_of_numbers = []
#     for i in range(length):
#         index = random.randint(0, 2)
#         list_of_numbers.append(round(random.uniform(-100, 100), index))
#     return list_of_numbers

# def FractionalPartList(list_of_numbers):
#     frac_part = []
#     for i in range(len(your_list)):
#         if round((abs(your_list[i]) % 1), 2) != 0:
#             frac_part.append(round((abs(your_list[i]) % 1), 2))
#     return frac_part

# len_of_list = int(input("Введите количество элементов списке: "))
# your_list = FillTheList(len_of_list)
# print(f'Ваш список случайных чисел: {your_list}')

# print(f'Масимальная дробная часть чисел в списке: {max(FractionalPartList(your_list))}')
# print(f'Минимальная дробная часть чисел в списке, отличная от "0": {min(FractionalPartList(your_list))}')
# print(f'Разница между максимальной и минимальной дробной частью: {round((max(FractionalPartList(your_list)) - min(FractionalPartList(your_list))), 2)}')

import random

len_of_list = int(input("Введите количество элементов списке: "))
your_list = [round(random.uniform(-100, 100), random.randint(0, 2)) for i in range(len_of_list)]
print(f'Ваш список случайных чисел: {your_list}')

frac_parts = list(map(lambda i: (abs(i)% 1), your_list))
frac_parts_not_null = [round(i, 2) for i in frac_parts if i != 0]

print(f'Разница между MAX и MIN дробной частью: {round((max(frac_parts_not_null) - min(frac_parts_not_null)), 2)}')