# Напишите программу, удаляющую из текста все слова, в которых присутствуют все буквы "а", "б", "в"

print('Редактированный текст:', " ".join(filter(
    lambda x: 'а' and 'в' and 'б' not in x, input('Введите текст: ').split())))