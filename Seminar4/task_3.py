# Задайте два числа.
# Напишите программу, которая найдёт наименьшее общее кратное этих двух чисел.

import math
import random

a = random.randint(0, 100)
b = random.randint(0, 100)

print(f'Заданные числа: {a}, {b}')
print('Наименьшее общее кратное:', (a * b) // math.gcd(a, b))
