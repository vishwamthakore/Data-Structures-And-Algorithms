class Queue:
    def __init__(self, limit=10):
        self.limit = limit
        self.queue = [None for i in range(limit)]
        self.front = -1
        self.rear = -1
        

    def __str__(self):
        op = ""
        if self.front == -1:
            return "None"

        curr = self.front
        while (curr!= self.rear):
            op+= str(self.queue[curr])
            op+= "--"
            curr = (curr + 1)%self.limit
        op += str(self.queue[curr])
        return op
    
    def enque(self, data):
        if self.front == -1:
            self.front = 0 
            self.rear = 0
            self.queue[self.rear] = data

        elif ((self.rear + 1)% self.limit == self.front):
            print("Queue is full")
        else:
            self.rear = (self.rear + 1)%self.limit
            self.queue[self.rear] = data

    def deque(self):
        if self.front == -1:
            print("Queue is already empty")
        elif (self.front == self.rear):
            res = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return res
        else:
            res = self.queue[self.front]
            self.front = (self.front +1)%self.limit
            return res
    
    def isFull(self):
        return (self.rear + 1)% self.limit == self.front

    def isEmpty(self):
        return (self.front == -1)


if __name__ == '__main__':
    q = Queue(5)
    print(q)
    for i in range(5):
        q.enque(i)
    print(q)
    q.enque(10)
    q.deque()
    q.deque()
    print(q)
    q.enque(11)
    print(q)

# Output
# None
# 0--1--2--3--4
# Queue is full
# 2--3--4
# 2--3--4--11
# deque([2, 3])

from collections import deque

q = deque()
q.append(1)
q.append(2)
q.append(3)
q.popleft()
print(q)
