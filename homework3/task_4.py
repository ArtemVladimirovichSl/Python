# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

import random

num = random.randint(0, 100)
print('Десятичное число:', num)

conv_num = ''
while num:
    conv_num = str(num % 2) + conv_num
    num //= 2

print('Двоичное число:', conv_num)
