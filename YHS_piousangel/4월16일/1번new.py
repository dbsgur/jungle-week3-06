import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('sample.txt')
input = sys.stdin.readline

n = int(input())

class Node :

    def __init__(self, item) :
        self.item = item
        self.left = None
        self.right = None
    
class BinaryTree() :

    def __init__(self):
        self.root = None

    def preorder(self, n):
        if n != None :
            print(n.item, end="")
            if n.left :
                self.preorder(n.left)
            if n.right :
                self.preorder(n.right)

    def inorder(self, n):
        if n!= None :
            if n.left :
                self.inorder(n.left)
            print(n.item, end="")
            if n.right :
                self.inorder(n.right)
    
    def postorder(self, n):
        if n!= None :
            if n.left :
                self.postorder(n.left)
            if n.right :
                self.postorder(n.right)
            print(n.item, end="")

tree = BinaryTree()

alpa_list = []
for i in range(n):
    x, y, z = map(str, input().split() )
    if i == 0:
        tree.root = Node(x)
    if y != '.' :
        Node(x).left = Node(y)
    if z != '.' :
        Node(x).right = Node(z)

print("tree.root", tree.root)
tree.preorder(tree.root)
tree.postorder(tree.root)

# n1 = Node('A')
# n2 = Node('B')
# n3 = Node('C')
# n4 = Node('D')
# n5 = Node('E')
# n6 = Node('F')
# n7 = Node('G')

# tree.root = n1
# n1.left = n2
# n1.right = n3
# n2.left = n4
# n3.left = n5
# n3.right = n6
# n6.right = n7