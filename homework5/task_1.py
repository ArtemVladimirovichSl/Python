# Напишите программу, удаляющую из текста все слова, в которых присутствуют все буквы "а", "б", "в"

import string

text = input('Введите текст: ').split()

lst = []
for i in (text):
    if 'а' not in i or 'б' not in i or 'в' not in i:
        lst.append(i)
    else:
        elem = list(i)
        for j in (elem [-1]):
            if j in string.punctuation:
                lst.append(j)

print(*lst)
