# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

nums = input('Введите 5 чисел через пробел: ').split()
max = int(nums[0])

for i in nums:
    if int(i) > max:
        max = int(i)

print('Наибольшее из введённых чисел =', max)
