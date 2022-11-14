# Напишите программу, удаляющую из текста все слова, в которых присутствуют все буквы "а", "б", "в"

import string

text = input('Введите текст: ').split()

lst = []
for word in text:
    w = word.lower()
    if not ('а' in w and 'б' in w and 'в' in w):
        lst.append(word)
    else:
        for j in (list(w) [-1]):
            if j in string.punctuation:
                lst.append(j)

print(*lst)
