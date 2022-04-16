# 1. 트리 순회(#1991)
import sys

sys.stdin = open('input.txt')
N = int(sys.stdin.readline())
nodeDict = {} # node 객체를 저장할 dict

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.preorder_str = ''
        self.inorder_str = ''
        self.postorder_str = ''

    def insert_root(self):
        self.root = Node('A')
        return self.root

    def insert_left(self, parent, value):
        parent.left = Node(value)
        return parent.left

    def insert_right(self, parent, value):
        parent.right = Node(value)
        return parent.right
    
    def preorder(self):
        # print('전위 순회')
        def preorder_node(node):
            self.preorder_str += node.value
            if node.left:
                preorder_node(node.left)
            if node.right:
                preorder_node(node.right)

        preorder_node(self.root)
        return self.preorder_str

    def inorder(self):
        # print('중위 순회')
        def inorder_node(node):
            if node.left:
                inorder_node(node.left)
            self.inorder_str += node.value
            if node.right:
                inorder_node(node.right)

        inorder_node(self.root)
        return self.inorder_str

    def postorder(self):
        # print('후위 순회')
        def postorder_node(node):
            if node.left:
                postorder_node(node.left)
            if node.right:
                postorder_node(node.right)
            self.postorder_str += node.value

        postorder_node(self.root)
        return self.postorder_str

bst = BinarySearchTree()
rootNode = bst.insert_root()
nodeDict['A'] = rootNode

for n in range(N):
    [root, left, right] = sys.stdin.readline().strip().split()
    
    if root in nodeDict:
        rootNode = nodeDict[root]

        if left != '.':
            leftNode = bst.insert_left(rootNode, left)
            nodeDict[left] = leftNode

        if right != '.':
            rightNode = bst.insert_right(rootNode, right)
            nodeDict[right] = rightNode

print(bst.preorder())
print(bst.inorder())
print(bst.postorder())
