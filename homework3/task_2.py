# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random

lst = [random.randint(0, 10) for i in range(random.randint(0, 10))]
print('Заданный список: ', lst)

new_lst = [lst[i] * lst[- i -1] for i in range((len(lst) + 1) // 2)]
print('Произведение пар чисел списка:', new_lst)
