class PriorityQueue:
    def __init__(self):
        self.data = []

    def parent(self, i):
        return (i-1)//2

    def leftchild(self, i):
        return (2 * i) + 1

    def rightchild(self, i):
        return (2 * i) + 2

    def upheapBubble(self, index):
        if index > 0:
            parentIndex = self.parent(index)
            if self.data[parentIndex][0] > self.data[index][0]:
                self.data[index],self.data[parentIndex] = self.data[parentIndex],self.data[index]
                self.upheapBubble(parentIndex)
    def downheapBubble(self,index):
        if index < (len(self.data)-1):
            leftchild = self.leftchild(index)
            rightchild = self.rightchild(index)
            if self.data[leftchild][0] < self.data[rightchild][0]:
                child = leftchild
            else:
                child = rightchild



            if self.data[child][0] < self.data[index][0]:
                self.data[index],self.data[child] = self.data[child],self.data[index]
                self.downheapBubble(child)

    def addItem(self,key,value):
        self.data.append((key,value))
        self.upheapBubble(len(self.data) - 1)

    def removeItem(self):
        self.data[0],self.data[len(self.data) - 1] = self.data[len(self.data) - 1],self.data[0]
        item = self.data[len(self.data)- 1]
        self.data.pop()
        self.downheapBubble(0)
        print(item)

    def Min(self):
        print(self.data[0])

    def length(self):
        print(len(self.data))

    def isEmpty(self):
        print(len(self.data) == 0)

PQ = PriorityQueue()
PQ.isEmpty()
PQ.length()
PQ.addItem(1,4)
PQ.addItem(6,3)
PQ.addItem(4,7)
PQ.addItem(10,2)
PQ.removeItem()
PQ.Min()
PQ.length()
PQ.isEmpty()