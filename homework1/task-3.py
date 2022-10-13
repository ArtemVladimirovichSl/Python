# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).

x = float(input('x = '))
y = float(input('y = '))
quarter_number = 4

if x == 0 or y == 0:
    print("Координата не должна быть ровна нулю")
else:
    if x > 0 and y > 0:
        quarter_number = 1
    elif x < 0 and y > 0:
        quarter_number = 2
    elif x < 0 and y < 0:
        quarter_number = 3
    print(f"Точка находится в {quarter_number} четверти плоскости")