class queue:
    def __init__(self):
        self.q = []

    def push(self,x):
        self.q.append(x)

        for i in range(len(self.q)):
            self.q.append(self.top())
            self.pop()

    def pop(self):
        if self.empty():
            return -1
        else:
            a = self.q.pop(self.top())
            return a
        
    def top(self):
        return -1 if self.empty else self.q[0]
    
    def empty(self):
        return len(self.q) == 0
    
    