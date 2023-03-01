class Node:
    def __init__(self,value):
        self.val = value
        self.next = None
        self.prev = None
        self.size = 0

class DoubleLinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None


    def insert(self,i ,newNode):
        if self.size == 0:
            self.head = newNode
            self.tail = newNode

        if i == 0:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

        elif i == self.size:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode

        else:
            temp = self.head
            index = 0
            while index < i -1:
                temp = temp.next
                index += 1

            newNode.next = temp.next
            newNode.prev = temp
            temp.next.prev = newNode
            temp.next = newNode

        self.size += 1

    def remove(self, i):
        if self.size == 0:
            print("Linked list is empty.")

        if i == 0:
            self.head = self.head.next

        elif i == self.size:
            self.tail = self.tail.prev

        else:
            temp = self.head
            index = 0
            while index < i-1:
                temp = temp.next
                index += 1
            temp.next = temp.next.next
        self.size -= 1


    def length(self):
        return self.size



    def printitems(self):
        temp = self.head
        while temp != None:
            print(temp.val)
            temp = temp.next



myList = DoubleLinkedList()
myList.insert(0,Node(5))
myList.insert(1,Node(10))
myList.insert(1,Node(50))
myList.insert(2,Node(3))

#myList.remove(0)



myList.printitems()


