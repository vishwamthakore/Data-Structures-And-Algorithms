class Node:
    def __init__(self, data, next=None, prev= None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtBeginning(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            temp = self.head
            self.head = newNode
            self.head.next = temp
            self.head.next.prev = self.head
    
    def insertAtEnd(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        
        curr = self.head
        while curr.next != None:
            curr= curr.next
        
        curr.next = newNode
        curr.next.prev = curr
        curr.next.next = None

    def deleteFromEnd(self):
        if self.head == 0:
            return
        elif self.head.next == None:
            self.head = None
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.prev.next = None
            curr = None
    
    def printList(self):
        curr = self.head
        while curr != None:
            print(curr.data, end = "<=>")
            curr = curr.next
        print("None")


if __name__== "__main__":
    dll = DoublyLinkedList()
    dll.printList()
    dll.insertAtBeginning(1)
    dll.printList()
    dll.insertAtBeginning(2)
    dll.printList()
    dll.insertAtBeginning(3)
    dll.printList()
    dll.insertAtEnd(4)
    dll.printList()
    dll.insertAtEnd(5)
    dll.printList()
    dll.deleteFromEnd()
    dll.printList()

# Output
# None
# 1<=>None
# 2<=>1<=>None
# 3<=>2<=>1<=>None
# 3<=>2<=>1<=>4<=>None
# 3<=>2<=>1<=>4<=>5<=>None
# 3<=>2<=>1<=>4<=>None