import time

class FiboIter():

    def __init__(self, max: int):
        self.limit = max

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            result = self.n1
        elif self.counter == 1:
            self.counter += 1
            result = self.n2
        else:
            self.aux = self.n1 + self.n2
            self.n1, self.n2 = self.n2, self.aux # swaping
            self.counter += 1
            result = self.aux
            
        if (result < self.limit):
            return result
        else:
            raise StopIteration

if __name__ == "__main__":
    fibonacci = FiboIter(5)
    for element in fibonacci:
        print(element)
        time.sleep(1)