class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtBeginning(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.head.next = self.head
        
        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            
            curr.next = newNode
            curr.next.next = self.head
            self.head = curr.next

    
    def printList(self):
        curr = self.head
        if self.head == None:
            print("None")
            return
        while curr.next != self.head:
            print(curr.data, end = "->")
            curr = curr.next
        print(curr.data)

if __name__== "__main__":
    cll = CircularLinkedList()
    cll.printList()
    cll.insertAtBeginning(1)
    cll.printList()
    cll.insertAtBeginning(2)
    cll.printList()
    cll.insertAtBeginning(3)
    cll.printList()