# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

import random

lst = [random.randint(99, 1000) / 100 for i in range(random.randint(1, 10))]
print('Заданный список: ', lst)

new_lst = [round(i % 1, 2) for i in lst]

print('Максимальное значение дробной части =', max(new_lst))
print('Минимальное значение дробной части =', min(new_lst))
print('Разница =', round(max(new_lst) - min(new_lst), 2))
