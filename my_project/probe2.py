import json

try:
    with open(input()) as file1:
        data1 = json.load(file1)
        print(data1)
except FileNotFoundError:
    print('Файл не найден')
except json.decoder.JSONDecodeError:
    print('Ошибка при десериализации')




