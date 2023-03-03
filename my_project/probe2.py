from datetime import datetime

with open('diary.txt', 'r', encoding='utf-8') as file:
    context = file.readlines()

    new_content = {}
    for string in context:

        if string.strip() == '':
            continue
        else:
            print(string.strip())

