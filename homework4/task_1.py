# Вычислить число c заданной точностью d


# ВАРИАНТ 1:
from math import pi

d = int(input('Задайте количество знаков после запятой для числа Пи: '))
print(f'Число Пи с заданной точностью {d} равно {round(pi, d)}')


# ВАРИАНТ 2:
import random
import decimal
num = random.uniform(0.5, 10.5)
correct = input('Задайте точность в формате \'0.001\': ')

d = abs(decimal.Decimal(correct).as_tuple().exponent)

print(f'Число {num} с заданной точностью {correct} равно {round(num, d)}')


# ВАРИАНТ 3: СЛУЧАЙНЫЕ ЧИСЛА
import random
num = random.uniform(0.5, 10.5)
degree = random.randint(-10, -1)
d = 10 ** degree

print(f'Число {num} с заданной точностью {d} равно {round(num, -degree)}')
