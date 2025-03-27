class stack:
    class node:
        def __init__(self,data):
            self.data = data
            self.next = None
    
    def __init__(self):
        self.head = None

    def push(self,x):
        new = self.node(x)
        new.next = self.head
        self.head = new

    def pop(self):
        if self.head is None:
            return -1
        pop = self.head.data
        self.head = self.head.next
        return pop
    
    def peek(self):
        return self.head.data
    
    def IsEmpty(self):
        return self.head == None
