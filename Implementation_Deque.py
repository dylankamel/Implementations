from self import self

class Deque:
    def __init__(self,n):
        self.data = [None] * n
        self.first = 0
        self.last = 0
        self.len = 0
        self.max_length = n


    def add_first(self,val):
        if(self.len > self.max_length):
            print("List is full")
        else:
            if(self.len == 0):
                self.data[self.first] = val
                self.first = (self.first - 1) % 10
                self.last = (self.last + 1) % 10
                self.len += 1
            else:
                self.data[self.first] = val
                self.first = (self.first - 1) % self.max_length
                self.len += 1


    def add_last(self,val):
        if (self.len > self.max_length):
            print("List is full")

        else:
            if (self.len == 0):
                self.data[self.first] = val
                self.last = (self.last + 1) % 10
                self.first = (self.first - 1) % 10
                self.len += 1
            else:
                self.data[self.last] = val
                self.last = (self.last + 1) % self.max_length
                self.len += 1


    def remove_first(self):
        if (self.len == 0):
            print("List is Empty")
        else:
            if (self.len == 1):
                temp = self.data[self.first + 1]
                self.data[self.first + 1] = None
                self.first = (self.first + 1) % self.max_length
                self.last = (self.last - 1) % self.max_length
                self.len -= 1
                print(temp)
            else:
                temp = self.data[self.first + 1]
                self.data[self.first + 1] = None
                self.first = (self.first + 1) % self.max_length
                self.len -= 1
                print(temp)


    def remove_last(self):
        if (self.len == 0):
            print("List is Empty")
        else:
            if (self.len == 1):
                temp = self.data[self.last - 1]
                self.data[self.last - 1] = None
                self.last = (self.last - 1) % self.max_length
                self.first = (self.first + 1) % self.max_length
                self.len -= 1
                print(temp)
            else:
                temp = self.data[self.last - 1]
                self.data[self.last - 1] = None
                self.last = (self.last - 1) % self.max_length
                self.len -= 1
                print(temp)

    def first(self):
        FV =  self.data[(self.first + 1) % 10]
        print(FV)

    def last(self):
        LV = self.data[(self.last - 1) % 10]
        print(LV)


    def length(self):
        counter = 0
        for i in self.data:
            if i == None:
                continue
            else:
                counter += 1
        print(counter)

    def is_empty(self):
        print(self.len == 0)

    def printdeque(self):
        for i in self.data:
            if i == None:
                continue
            else:
                print(i)







