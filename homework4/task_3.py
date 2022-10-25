# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# ВАРИАНТ 1: УДАЛЕНИЕ ДУБЛИРУЮЩИХ ЭЛЕМЕНТОВ ИЗ СПИСКА
import random

lst = [random.randint(0, 10) for i in range(10)]
print('Заданный список: ', *lst)

new_lst = []
for i in lst:
    if i not in new_lst:
        new_lst.append(i)

print('Список из неповторяющихся элементов:', new_lst)

# ВАРИАНТ 2: ВЫВОД ЭЛЕМЕНТОВ, ВСТРЕЧАЮЩИХСЯ ОДИН РАЗ
import random

lst = [random.randint(0, 10) for i in range(10)]
print('Заданный список: ', *lst)

answ = []
for i in lst:
    if lst.count(i) == 1:
        answ.append(i)

print('Список элементов, встречающихся один раз:', answ)
