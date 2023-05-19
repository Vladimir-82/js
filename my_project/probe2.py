class DictItemsIterator:

    def __init__(self, data):
        self.data = data



    def __iter__(self):
        return self

    def __next__(self):
        for key, val in self.data.items():
            return key, val


pairs = DictItemsIterator({1: 'A', 2: 'B', 3: 'C'})

print(*pairs)


