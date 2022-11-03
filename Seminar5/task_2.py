# Дан список чисел.
# Создайте список, в который попадают числа, описываемые возрастающую последовательность.
# Порядок элементов менять нельзя.

import random

lst = [random.randint(0, 9) for i in range(9)]
print('Заданный список:', lst)

# ВАРИАНТ №1:

new_lst = [lst[0]]
for i in lst:
    if i > max(new_lst):
        new_lst.append(i)

print('Итоговый список:', new_lst)

# ВАРИАНТ №2:

new_lst = []
for i in range(len(lst)):
    if lst[i] == max(lst[:i+1:]) and lst[i] not in new_lst:
        new_lst.append(lst[i])

print('Итоговый список:', new_lst)
