# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

num = int(input("Введите число: "))
first_prime = 2

lst = []
while first_prime <= num:
    if num % first_prime == 0:
        lst.append(first_prime)
        num //= first_prime
    else:
        first_prime += 1

print('Cписок простых множителей заданного числа:', lst)
