class Dog:
    def __init__(self, name='initname', typ='inityp'):
        self.name = name
        self.typ = typ


    def __str__(self):
        return f'{self.name, self.typ}'

isinst = Dog(name='ist_name', typ='ins_type')

print(isinst)
