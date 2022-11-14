# Реализуйте RLE алгоритм: реализуйте модуль сжатия данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('RLE_decoded.txt', 'r') as file:
    my_text = file.read()
text = ''.join(my_text)

def encode_rle(text):
    str_code = ''
    count = 1
    for i in range(len(text) -1):
        if text[i] == text[i + 1]:
            count += 1
            if count == 9:
                str_code += str(count) + text[i]
                count = 1
        else:
            str_code += str(count) + text[i]
            count = 1
    if count > 1 or text[len(text) - 2] != text[-1]:
        str_code += str(count) + text[-1]
    return str_code


str_code = encode_rle(text)
file = open('RLE_encoded.txt', 'w').write(str_code)

print(f'Данные из файла: {my_text}\n\
Сжатые данные: {str_code}')
