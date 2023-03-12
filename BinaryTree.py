class Node:
    def __init__(self,val):
        self.value = val
        self.parent = None
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def addNode(self,parentNode,newNode):
        if self.root == None:
            self.root = newNode

        elif parentNode.left == None:
            parentNode.left = newNode
            newNode.parent = parentNode

        elif parentNode.right == None:
            parentNode.right = newNode
            newNode.parent = parentNode

        else:
            print("Parent node has 2 child nodes Already")

    def removeNode(self,node):
        #for if the node given has 0 child nodes
        if node.left == None and node.right == None:
            # if the node is a left child of its parent node
            if node == node.parent.left:
                node.parent.left == None
            # if the node is the right child of it's parent node
            else:
                node.parent.right == None

        # for if the node given has 2 child nodes it won't be possible to remove
        elif node.left != None and node.right != None:
            print("Node given cannot be removed")
        # for if the node given has 1 child node
        else:
            child = None
            # here we find if the left or right pointer has a given value and set it to child
            if node.left != None:
                child = node.left
            else:
                child = node.right

            # with the val set to child we now change the pointer to the parent of the node removed
            if node == node.parent.left:
                node.parent.left = child

            else:
                node.parent.right = child

    def depth(self,node):
        if node == self.root:
            return 0
        else:
            return 1 + self.depth(node.parent)

    def height(self,node):
        if node == None:
            return 0
        else:
            x = self.height(node.left)
            y = self.height(node.right)
            return max(x+1,y+1)

    
    def printInOrder(self,node):
        if node != None:
            self.printInOrder(node.left)
            print(node.value)
            self.printInOrder(node.right)

    def printPreOrder(self,node):
        if node != None:
            print(node.value)
            self.printPreOrder(node.left)
            self.printPreOrder(node.right)

    def printPostOrder(self,node):
        if node != None:
            self.printPostOrder(node.left)
            self.printPostOrder(node.right)
            print(node.value)

A = Node(50)
B = Node(30)
C = Node(0)
D = Node(20)
E = Node(25)
F = Node(40)
G = Node(12)

BT = BinaryTree()
BT.addNode(None,A)
BT.addNode(A,B)
BT.addNode(A,C)
BT.addNode(B,D)
BT.addNode(B,E)
BT.addNode(C,F)
BT.addNode(C,G)
BT.printPostOrder(A)

