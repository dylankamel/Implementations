from self import self


class Queue:
    def __init__(self, n):
        self.data = [None] * n
        self.first = 0
        self.index = 0
        self.max = n
        self.len = 0


    def Enqueue(self,val):
        self.data[self.index] = val
        self.index = (self.index + 1) % self.max
        self.len += 1

    def Dequeue(self):
        if self.isEmpty() == True:
            return "Empty"
        else:
            temp = self.data[self.first]
            self.data[self.first] = None
            self.first = (self.first + 1) % self.max
            self.len -= 1
            return temp

    def First(self):
        if self.isEmpty == True:
            return "Empty"
        else:
            return self.data[self.first]

    def Length(self):
        return self.len

    def isEmpty(self):
        return self.len == 0

test = Queue(10)
test.Enqueue(1)
test.Enqueue(2)
print(test.Dequeue())
print(test.First())
print(test.Length())
print(test.isEmpty())
