try:
    file = open(input(), 'r', encoding='utf-8')
    text = file.read()
    print(text)

except:
    print('Файл не найден')
