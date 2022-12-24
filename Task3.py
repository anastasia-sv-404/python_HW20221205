# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('input_task3.txt', 'r', encoding='UTF-8') as file:
    string = file.readline()
print(string)

def rle_zip(text):
    new_text = ''
    i = 0
    while i < len(text):
        count = 1
        while i + 1 < len(text) and text[i] == text[i + 1]:
            count += 1
            i = i + 1
        new_text += f'{count}{text[i]}'
        i += 1
    return new_text

string_zip = rle_zip(string)
print(string_zip)


def rle_unzip(text_zip):
    list_numbers = []
    list_items = []
    for i in text_zip:
        if i.isdigit():
            list_numbers.append(int(i))
        else:
            list_items.append(i)

    text_unzip = ''
    for i in range(len(list_numbers)):
        text_unzip += f'{list_items[i] * list_numbers[i]}'

    return text_unzip

string_unzip = rle_unzip(string_zip)
print(string_unzip)

with open('output_task3.txt', 'w', encoding='UTF-8') as file:
    file.write(string_unzip)
