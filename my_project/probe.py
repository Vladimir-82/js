with open('input.txt', 'r', encoding='utf-8') as file:
    text = file.readlines()

with open('output.txt', 'w', encoding='utf-8') as file:
    for num, el in enumerate(text):
        print(str(num + 1) + ') ' + el.rstrip(), file=file)





