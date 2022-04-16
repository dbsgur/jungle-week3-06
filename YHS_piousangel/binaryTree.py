class Node:
    def __init__(self, item):
        self.item = item        #자기 자신의 값
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self): #트리 생성
        self.root = None
    
    # 트리 높이
    def height(self, root):
        if root == None:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1

    # 전위 순회
    def preorder(self, n):
        if n!= None:
            print(n.item, '', end='') #노드 방문
            if n.left:
                self.preorder(n.left) #왼쪽 서브트리 순회
            if n.right:
                self.preorder(n.right) #오른쪽 서브트리 순회

    # 후위 순회
    def postorder(self, n):
        if n != None:
            if n.left:
                self.postorder(n.left)
            if n.right:
                self.postorder(n.right)
            print(n.item, '', end='') # 노드 방문

    # 중위 순회
    def inorder(self, n):
        if n != None:
            if n.left:
                self.inorder(n.left)
            print(n.item, '', end='') # 노드 방문
            if n.right:
                self.inorder(n.right)

    # 레벨 순회
    def levelorder(self, n):
        q = []
        q.append(n)
        while q:
            t = q.pop(0)
            print(t.item, '', end='')
            if t.left != None:
                q.append(t.left)
            if t.right != None:
                q.append(t.right)


# 트리를 읽을 때 대전제는 왼쪽부터 오른쪽으로 읽는것
# 이진 트리는 깊이 h에 최대 2^(h-1)만큼의 노드를 가질수 있다

tree = BinaryTree()
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)
n6 = Node(60)
n7 = Node(70)
n8 = Node(80)

tree.root = n1
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
n4.left = n8

print('트리 높이 : ', tree.height(tree.root))

print('전위 순회 : ', end=' ')
tree.preorder(tree.root)
print()

print('후위 순회 : ', end=' ')
tree.postorder(tree.root)
print()

print('중위 순회 : ', end=' ')
tree.inorder(tree.root)
print()

print('레벨 순회 : ', end=' ')
tree.levelorder(tree.root)
print()