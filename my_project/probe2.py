class Fibonacci:

    def __init__(self):
        self.a = 1
        self.b = 1
        self.start = 1


    def __iter__(self):
        return self

    def __next__(self):
        if self.start:
            return self.start
        del self.start
        self.a, self.b = self.b, self.a + self.b
        return self.a

fibonacci = Fibonacci()

print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
