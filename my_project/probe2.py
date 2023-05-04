from collections import defaultdict



def remove_marks(text, marks):

    remove_marks.__dict__.setdefault('count', 0)
    text = ''.join(filter(lambda x: x not in marks, text))
    remove_marks.count += 1
    return text

text = 'Hi! Will we go together?'

print(remove_marks(text, '!?'))
print(remove_marks.count)