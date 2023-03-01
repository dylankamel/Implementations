class Stack:
    def __init__(self, n):
        self.count = 0
        self.data = [None] * n
        self.max = n
        self.top = 0



    def push(self, val):
        if self.count == self.max:
            print("Stack is full")
        else:
            self.data[self.count] = val
            self.count += 1


    def pop(self):
        if self.count == 0:
            print("Empty")
        else:
            temp = self.data[self.count - 1]
            self.data[self.count - 1] = None
            self.count -= 1
            print(temp)

    def top(self):
        if self.isEmpty() == True:
            print("Empty")
        else:
            return self.data[self.top]



    def length(self):
        print(self.count)


    def isEmpty(self):
        print(self.count == 0)

    def printStack(self):
        index = 0
        while index < self.count:
            print(self.data[index])
            index += 1
            













