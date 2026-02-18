class FibonacciIterator:
    def __init__(self, max_elements):
        self.max_elements = max_elements
        self.count = 0
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_elements:
            raise StopIteration

        if self.count == 0:
            result = self.a
        elif self.count == 1:
            result = self.b
        else:
            self.a, self.b = self.b, self.a + self.b
            result = self.b

        self.count += 1
        return result
