from random import randrange


class Hashtable:
    def __init__(self,N):
        self.P = 109345121
        self.a = 1 + randrange(self.P-1)
        self.b = randrange(self.P)
        self.n = N
        self.table = [None] * N

    def hashfunction(self, key):
        return (((hash(key) * self.a) + self.b) % self.P) % self.n


    def setItem(self,key,value):
        index = self.hashfunction(key)
        if self.table[index] == None:
            self.table[index] = (key,value)

        elif type(self.table[index]) is tuple:
            if self.table[index][0] == key:
                self.table[index] = (key,value)
            else:
                temp = []
                temp.append(self.table[index])
                temp.append((key,value))
                self.table[index] = temp
        else:
            bPresent = False
            for i in range(len(self.table[index])):
                if self.table[index][i][0] == key:
                    self.table[index][i] = (key,value)
                    bPresent = True
            if bPresent == False:
                self.table[index].append((key,value))


    def getItem(self,key):
        index = self.hashfunction(key)
        if self.table[index] == None:
            return None

        elif type(self.table[index]) is tuple:
            if self.table[index][0] == key:
                return self.table[index][1]

        else:
            value = None
            for i in range(len(self.table[index])):
                if self.table[index][i][0] == key:
                    value = self.table[index][i][1]
                    break
            return value

    def removeItem(self,key):
        index = self.hashfunction(key)
        if self.table[index] == None:
            print("There is no value at that key")

        elif type(self.table[index]) is tuple:
            if self.table[index][0] == key:
                val = self.table[index][1]
                self.table[index][1] = None
                return val

        else:
            value = None
            for i in range(len(self.table[index])):
                if self.table[index][i][0] == key:
                    value = self.table[index][i][1]
                    self.table[index][i][1] = None
                    break
            return value

    def printhashtable(self):
        print(self.table)

HT = Hashtable(7)
HT.setItem('A',100)
HT.setItem('B',200)
HT.setItem('C',300)
HT.setItem('D',400)
HT.setItem('E',500)
HT.setItem('F',600)
HT.setItem('G',700)
HT.setItem('H',800)
HT.setItem('I',900)
HT.setItem('J',1000)
HT.setItem('K',1100)
HT.setItem('L',1200)
HT.setItem('M',1300)
HT.setItem('N',1400)
HT.setItem('O',1500)
print(HT.getItem('A'))
print(HT.getItem('B'))
print(HT.getItem('C'))
HT.printhashtable()


