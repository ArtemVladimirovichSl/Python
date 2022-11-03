# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

from random import randint, choice

messages = ['Ваша очередь брать конфеты', 'возьмите конфеты',
            'сколько конфет возьмёте?', 'берите, не стесняйтесь', 'Ваш ход', 'не в чем себе не отказыаайте']

def input_dat(name):
    x = int(
        input(f"{name}, {choice(messages)}: "))
    while x < 1 or x > 28:
        x = int(
            input(f"{name}, введите количество конфет из указанного диапазона: "))
    return x


def p_print(name, k, counter, value):
    print(
        f"{name} взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")


print('Рады приветствовать вас в игре, по условиям которой вам даётся 2021 конфета.\n\
Вам нужно по очереди забирать какое-то количество конфет, но не более 28 за ход.\n\
Выигрывает тот, кто заберёт последнюю конфету. Ему достаются все конфеты проигравшего.\n\
Итак, начнём!')
player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
if player1 == player2:
    print('Измените одно имя, иначе мы запутаемся')
else:
    print('Бросим жребий на право первого хода. Орёл или решка?')
    draw1 = input(f'{player1}: ')
    draw2 = input(f'{player2}: ')
    if draw1 != draw2:
        if draw1.lower() == 'орёл' or draw1.lower() == 'решка':
            if draw2.lower() == 'орёл' or draw2.lower() == 'решка':
                flag = randint(1, 2)
                if flag == 1:
                    print(f"Выпало {draw1}, первый ходит {player1}")
                else:
                    print(f"Выпало {draw2}, первый ходит {player2}")
            else:
                print(f'{player2}, будьте внимательнее при вводе')
        else:
            print(f'{player1}, будьте внимательнее при вводе')
    else:
        print('Некорректный ввод, попробуйте ещё раз')

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
                    f"{player1} взял {k}, теперь у него {counter1}. На столе больше не осталось конфет.")
        else:
            print(f'На столе осталось {value} конфет')
    else:
        k = input_dat(player2)
        if k <= value:
            counter2 += k
            value -= k
            flag = True
            if value > 0:
                p_print(player2, k, counter2, value)
            else:
                print(
                    f"{player2} взял {k}, теперь у него {counter2}. На столе больше не осталось конфет.")
        else:
            print(f'На столе осталось {value} конфет')

if flag:
    print(f"Выиграл {player2}, ему достаются все конфеты опонента")
else:
    print(f"Выиграл {player1}, ему достаются все конфеты опонента")
