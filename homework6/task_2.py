# Дана последовательность чисел.
# Получить список уникальных элементов заданной последовательности,
# список повторяемых, и убрать дубликаты из заданной последовательности.

numbers = [1, 2, 3, 5, 1, 5, 3, 10]


def unique(numbers): return sorted(
    list(set(x for x in numbers if numbers.count(x) == 1)))


def repeatable(numbers): return sorted(
    list(set(x for x in numbers if numbers.count(x) > 1)))


print(f'Заданная последовательность: {numbers}\n\
Список уникальных элементов: {unique(numbers)}\n\
Список повторяемых элементов: {repeatable(numbers)}\n\
Список без дубликатов: {list(set(numbers))}')
