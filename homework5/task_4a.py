# Реализуйте RLE алгоритм: реализуйте модуль Восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('RLE_encoded.txt', 'r') as file:
    my_text = file.read()
text = ''.join(my_text)


def decoding_rle(text):
    str_decode = ''
    for i in range(0, len(text), 2):
        str_decode += text[i + 1] * int(text[i])
    return str_decode


str_decode = decoding_rle(text)
file = open('RLE_decoded.txt', 'w').write(str_decode)

print(f'Данные из файла: {my_text}\n\
Восстановленные данные: {str_decode}')
