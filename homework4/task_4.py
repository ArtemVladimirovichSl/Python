# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена.
# Записать в файл многочлен степени k.

import random

def write_file(st):
    n = int(random.randint(1, 2))                 # создаём 2 файла для записи результатов
    with open(f'file_{n}.txt', 'w') as data:      # с возможностью случайного обновления
        data.write(st)                            # то одного, то другого файла


def rnd(): return random.randint(0, 101)          # создание случайных значений многочлена


def create_mn(k):                                 # создание коофициентов
    lst = [rnd() for i in range(k+1)]
    return lst


def create_str(sp):                              # создание многочлена в виде строки
    lst = sp[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}x'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += ' = 0'
    return wr


k = int(input('Введите натуральную степень: '))
write_file(create_str(create_mn(k)))                              # запись в файл
