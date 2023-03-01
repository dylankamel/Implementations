class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0


    def insert(self, i, newNode):
       temp = self.head

       if i == 0:
           if self.size == 0:
               self.head = newNode
               self.size += 1
           else:
               newNode.next = self.head
               self.head = newNode
               self.size += 1

       else:
            index = 0
            while (index < i-1):
                temp = temp.next
                index += 1
            newNode.next = temp.next
            temp.next = newNode
            self.size += 1

    def remove(self, i):
        if self.size == 0:
            print("Linked List is Empty")

        if i == 0: #Begining of List
            self.head = self.head.next
            self.size -= 1

        else:
            temp = self.head
            index = 0
            while(index < i-1):
                temp = temp.next
                index += 1
            if i == self.size-1: # if Removing at the end of list
                temp.next = None
                self.size -= 1
            else: # if removing in the middle of the list
                temp.next = temp.next.next
                self.size -= 1

    def length(self):
        return self.size


    def printItems(self):
        temp = self.head
        while temp != None:
            print(temp.val)
            temp = temp.next



myList = SingleLinkedList()
myList.insert(0,Node(5))
myList.insert(1,Node(2))
myList.insert(1,Node(4))
myList.remove(2)

print(myList.length())



myList.printItems()







