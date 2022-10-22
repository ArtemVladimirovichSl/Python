# Задайте число.
# Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

num = int(input('Введите число: '))

fib = []
for i in range(num + 1):
    if i == 0:
        fib.append(0)
    elif i == 1:
        fib.append(1)
    else:
        fib.append(fib[i-1] + fib[i-2])

neg = [(((-1) ** (i + 1)) * fib[i]) for i in range(num, 0, -1)]
print(neg + fib)
