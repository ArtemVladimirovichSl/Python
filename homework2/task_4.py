# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

import random

n = int(input('Задайте количество элементов: '))
lst = []
for i in range(n):
    lst.append(random.randint(-n, n))
print('Созданный список: ', lst)

prod = 1
new_lst = []

with open('file.txt', 'r') as file:
    for line in file:
        if -len(lst) <= int(line) < len(lst):
            prod *= lst[int(line)]
            new_lst.append(lst[int(line)])

print('Список после отбора элементов: ', new_lst)
print('Произведение элементов на указанных позициях = ',
      prod if prod != 1 else 'Значения не найдены')
