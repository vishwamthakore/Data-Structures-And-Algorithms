class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right  = None

# Find number of nodes
def size(node):
    if node == None:
        return 0
    return 1 + size(node.left) + size(node.right)

# Find the height
def height(node):
    if node == None:
        return 0
    return 1 + max(height(node.left), height(node.right))

# Find max in tree
def maximum(node):
    if node == None:
        return float('-inf')
    
    max_left = maximum(node.left)
    max_right = maximum(node.right)

    return max([node.data, max_left, max_right])

# Search
def search(node, val):
    if node == None:
        return False
    left = search(node.left, val)
    right = search(node.right, val)

    if (left == True or right == True or node.data == val):
        return True
    else:
        return False


if __name__ == "__main__":
    n1 = Node(10)
    n2 = Node(5)
    n3 = Node(15)
    n4 = Node(35)
    n5 = Node(36)

    n1.left = n2
    n1.right = n3
    n3.right = n4
    n4.right = n5

    print(size(n1))
    print(height(n1))
    print(maximum(n1))
    print(search(n1, 36))
    print(search(n1, 34))

# Output
# 5 (size)
# 4 (height)
# 36 (Max)
# True (search)
# False (search)
