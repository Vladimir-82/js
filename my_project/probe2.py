lg = {'en': 'abcdefghijklmnopqrstuvwxyz', 'ru': 'абвгдежзийклмнопрстуфхцчшщъыьэюя'}

class Alphabet:

    def __init__(self, language):
        self.language = language
        self.iterator = iter(lg[language])





    def __iter__(self):
        return self


    def __next__(self):
        try:
            return next(self.iterator)
        except:
            self.iterator = iter(lg[self.language])
            return next(self.iterator)


en_alpha = Alphabet('en')

letters = [next(en_alpha) for _ in range(28)]

print(*letters)