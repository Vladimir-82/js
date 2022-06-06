# Get the Middle Character
def get_middle(s):
    return s[len(s)//2-1:len(s)//2 + 1] if not len(s) % 2 else s[len(s)//2]


print(get_middle('test'))