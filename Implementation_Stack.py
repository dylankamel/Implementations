from self import self

class Stack:
    def __init__(self, n):
        self.count = 0
        self.data = [None] * n
        self.max = n


    #pop inserts a data item at the end of the list
    def push(self, val):
        if self.count == self.max:
            print("Stack is full")
        else:
            self.data[self.count] = val
            self.count = self.count + 1

    # removes and returns the last inserted data item
    def pop(self):
        if self.isEmpty() == True:
            return "Empty"
        else:
            temp = self.data[self.count - 1]
            self.data[self.count - 1] = None
            self.count -= 1
            return temp

    # returns the last inserted value
    def top(self):
        if self.isEmpty() == True:
            return "Empty"
        else:
            return self.data[self.count - 1]


    # returns the number of data items in the list
    def length(self):
        return self.count

    # returns a true or false value if there is data in the list
    def isEmpty(self):
        return self.count == 0

# First round
test = Stack(10)













