def convert(some_string):
    counter = 0
    big = 0
    for item in some_string:
        if item.isalpha():
            counter += 1
            if item.istitle():
                big += 1
    return some_string.upper() if big > counter // 2 else some_string.lower()



print(convert('BEAEQgeek'))






