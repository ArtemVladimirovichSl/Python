# Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.

num = int(input('Введите n: '))
sum = 0
lst = []

for i in range(1, num+1):
    lst.append((1 + 1 / i) ** i)
    sum += (1 + 1 / i) ** i

print(f'{lst} - список из {num} чисел последовательности (1 + 1 / n) ** n')
print(f'{sum} - сумма из чисел этого списка')
