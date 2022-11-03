# Реализуйте RLE алгоритм: реализуйте модуль сжатия данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('RLE_decoded.txt', 'r') as file:
    my_text = file.read()


def encode_rle(ss):
    str_code = ''
    prev_char = ''
    count = 1
    for char in my_text:
        if char != prev_char:
            if prev_char:
                str_code += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    return str_code


str_code =  encode_rle(my_text)
file = open('RLE_encoded.txt', 'w')
file.write(str_code)
print(f'Данные из файла: {my_text}\n\
Сжатые данные: {str_code}')
