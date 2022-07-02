from SinglyLinkedList import *

sll = SinglyLinkedList()
for i in range(10):
    sll.insertAtBeginning(i)

sll.print_ll()

def reverseLinkedList(sll):
    curr = sll.head

    while curr != None:
        if curr == sll.head:
            temp = curr
            curr = curr.next
            temp.next = None
        else:
            currNext = curr.next
            curr.next = temp
            temp =curr
            curr = currNext
        sll.head = temp

reverseLinkedList(sll)
sll.print_ll()


# Output
# 9 ->8 ->7 ->6 ->5 ->4 ->3 ->2 ->1 ->0 ->None
# 0 ->1 ->2 ->3 ->4 ->5 ->6 ->7 ->8 ->9 ->None