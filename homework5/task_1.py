# Напишите программу, удаляющую из текста все слова, в которых присутствуют все буквы "а", "б", "в"

import string

text = input('Введите текст: ').split()

lst = []
for i in text:
    if not ('а' in i and 'б' in i and 'в' in i):
        lst.append(i)
    else: 
        for j in (list(i) [-1]):
            if j in string.punctuation:
                lst.append(j)

print(*lst)
