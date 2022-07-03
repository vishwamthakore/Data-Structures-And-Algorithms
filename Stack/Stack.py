class Stack:
    def __init__(self, limit=10):
        self.stack = []
        self.limit = limit

    def push(self, val):
        if len(self.stack) >= self.limit:
            print("Stack Overflow")
        else:
            self.stack.append(val)
    
    def pop(self):
        if len(self.stack) <=0:
            print("Stack Underflow")
            return
        else:
            return self.stack.pop()
    
    def peek(self):
        if len(self.stack) <=0:
            print("Stack Underflow")
            return -1
        else:
            return self.stack[-1]
    
    def printStack(self):
        print(self.stack)

s = Stack()
s.push(1)
s.printStack()
s.push(2)
s.printStack()
s.push(3)
s.printStack()
s.push(4)
s.printStack()
print("Popped", s.pop())
print("Popped", s.pop())
print("Peek", s.peek())
s.printStack()