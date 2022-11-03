# Создайте программу для игры с конфетами человек против бота.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.

from random import randint, choice

messages = ['Ваша очередь брать конфеты', 'возьмите конфеты',
            'сколько конфет возьмёте?', 'берите, не стесняйтесь', 'Ваш ход', 'не в чем себе не отказывайте'
            ]


def input_dat(name):
    x = int(
        input(f"{name}, {choice(messages)}: "))
    while x < 1 or x > 28:
        x = int(
            input(f"{name}, введите количество конфет из указанного диапазона: "))
    return x


def p_print(k, counter, value):
    print(
        f"Вы взяли {k}, теперь у Вас {counter}. Осталось на столе {value}.")


def bot_print(k, counter, value):
    print(f'Я взял {k}, теперь у меня {counter}. Осталось на столе {value}.')


print('Рады приветствовать вас в игре, по условиям которой вам даётся 2021 конфета.\n\
Вам нужно по очереди забирать какое-то количество конфет, но не более 28 за ход.\n\
Выигрывает тот, кто заберёт последнюю конфету. Ему достаются все конфеты проигравшего.\n\
Итак, начнём!')
player1 = input('Давайте знакомиться! Как к Вам можно обращаться?: ')
player2 = 'Робик'
print(f'Очень приятно, {player1}! Меня зовут {player2}.\n\
Давайте бросим жребий на право первого хода.')
draw1 = input('Орёл или решка?: ')
if draw1.lower() == 'орёл' or draw1.lower() == 'решка':
    if draw1.lower() == 'орёл':
        draw2 = 'решка'
    elif draw1.lower() == 'решка':
        draw2 = 'орёл'
    print(f'Тогда у меня {draw2}')
    flag = randint(1, 2)
    if flag == 1:
        print(f"Выпало {draw1}, первый ходите Вы")
    else:
        print(f"Выпало {draw2}, первый хожу я")
else:
    print(f'{player1}, будьте внимательнее при вводе')

counter1 = 0
counter2 = 0
value = 2021

while value > 0:
    if flag == 1:
        k = input_dat(player1)
        if k <= value:
            counter1 += k
            value -= k
            flag = False
            if value > 0:
                p_print(player1, k, counter1, value)
            else:
                print(
                    f"Вы взяли {k}, теперь у Вас {counter1}. На столе больше не осталось конфет.")
        else:
            print(f'На столе осталось {value} конфет')
    else:
        if value >= 28:
            k = randint(1, 29)
            counter2 += k
            value -= k
            flag = True
            bot_print(k, counter2, value)
        elif value < 28:
            k = randint(1, value)
            counter2 += k
            value -= k
            flag = True
            bot_print(k, counter2, value)


if flag:
    print(f"Ура! Я выиграл! Мне достаются все Ваши конфеты.")
else:
    print(f"Поздравляю! Вы выиграли! Вам достаются все мои конфеты.")
