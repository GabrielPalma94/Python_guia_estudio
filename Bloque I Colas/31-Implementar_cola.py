from collections import deque
class cola:
    def __init__(self):
        self.cola = deque()
    def enqueue(self, x):
        self.cola.append(x)
    def dequeue(self):
        if not self.cola:
            raise IndexError
        else:
            return self.cola.popleft()
    def peek(self):
        if not self.cola:
            raise IndexError
        else:
            return self.cola[0]
    def is_empty(self):
        return not self.cola
    def size(self):
        return len(self.cola)   
c = cola()
c.enqueue(10)
c.enqueue(20)
c.enqueue(30)
print(c.dequeue())
print(c.peek())