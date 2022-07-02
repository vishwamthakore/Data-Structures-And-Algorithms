class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None


    def insertAtBeginning(self, data):
        "Inserts element at the beginning"    
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            self.head = new_node
            self.head.next = temp

    def insertAtIndex(self, data, index=0):
        if index == 0:
            self.insertAtBeginning(data)
        else:
            new_node = Node(data)
            curr = self.head
            curr_index = 0
            while curr_index < index-1:
                if curr == None:
                    return
                curr_index+=1
                curr = curr.next
            temp = curr.next
            curr.next = new_node
            new_node.next = temp

    def length(self):
        "Finds the length of Linked List"

        curr = self.head
        length = 0
        while curr is not None:
            length+=1
            curr = curr.next
        return length
    
    def print_ll(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, "->", end="")
            current_node = current_node.next
        print("None")





if __name__ == "__main__":
    sll= SinglyLinkedList()
    help(sll.insertAtBeginning)
    sll.insertAtBeginning(1)
    sll.insertAtBeginning(2)
    sll.insertAtBeginning(3)
    sll.insertAtIndex(5, 1)
    sll.print_ll()