# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*.
# Приоритет операций стандартный.
# Добавьте возможность использования скобок, меняющих приоритет операций

# ВАРИАНТ 1:   ОПАСНЫЙ
# print('Результат:', eval(input('Задайте арифметическое выражение: ')))


operators = {'+': (1, lambda x, y: x + y), '-': (1, lambda x, y: x - y),        # ВАРИАНТ 2:  ПАРСЕР
             '*': (2, lambda x, y: x * y), '/': (2, lambda x, y: x / y)}


def parse(line):
    num = ''
    for i in line:
        if not num and i in '-':
            num += i
            continue
        if i in '1234567890.':
            num += i
        elif num:
            yield int(num)
            num = ''
        if i in operators or i in '()':
            yield i
    if num:
        yield int(num)


def sort(parsed):
    tmp = []
    for i in parsed:
        if i in operators:
            while tmp and tmp[-1] != '(' and operators[i][0] <= operators[tmp[-1]][0]:
                yield tmp.pop()
            tmp.append(i)
        elif i == ')':
            while tmp:
                x = tmp.pop()
                if x == '(':
                    break
                yield x
        elif i == '(':
            tmp.append(i)
        else:
            yield i
    while tmp:
        yield tmp.pop()


def calc(sort):
    tmp = []
    for i in sort:
        if i in operators:
            y = tmp.pop()
            x = tmp.pop()
            tmp.append(operators[i][1](x, y))
        else:
            tmp.append(i)
    return tmp[0]


print('Результат: ', calc(sort(parse(input('Задайте арифметическое выражение: ')))))
