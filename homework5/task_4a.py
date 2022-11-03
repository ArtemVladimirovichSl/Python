# Реализуйте RLE алгоритм: реализуйте модуль Восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('RLE_encoded.txt', 'r') as file:
    my_text = file.read()


def decoding_rle(ss: str):
    count = ''
    str_decode = ''
    for char in ss:
        if char.isdigit():
            count += char
        else:
            str_decode += char * int(count)
            count = ''
    return str_decode


str_decode = decoding_rle(my_text)
file = open('RLE_decoded.txt', 'w')
file.write(str_decode)
print(f'Данные из файла: {my_text}\n\
Восстановленные данные: {str_decode}')
