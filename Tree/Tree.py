class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
class Tree:
    def __init__(self):
        self.root = None
    
    def inorder(self, node):
        if node == None:
            return
        self.inorder(node.left)
        print(node.data, end= " ")
        self.inorder(node.right)

    def preorder(self, node):
        if node == None:
            return
        print(node.data, end = " ")
        self.preorder(node.left)
        self.preorder(node.right)


if __name__ == "__main__":
    t = Tree()
    n1 = Node(10)
    n2 = Node(5)
    n3 = Node(15)
    n4 = Node(25)
    n1.left = n2
    n1.right = n3
    n3.right = n4
    t.root = n1
    t.inorder(t.root)
    print()
    t.preorder(n1)

# Output
# 5 10 15 25 
# 10 5 15 25