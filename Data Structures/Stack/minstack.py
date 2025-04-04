class MinStack:

    def __init__(self):
        self.s = []
        self.min = float('inf')
    
    def IsEmpty(self):
        return len(self.s) == 0
    
    def push(self,x):
        if self.isEmpty():
            self.s.append(x)
            self.min = x
        else:
            if x >= self.min: 
                self.s.append(x)
            else:
                self.s.append(2*x-min)
                self.min = x
        
    def pop(self):
        if self.IsEmpty():
            return
        
        val = self.s.pop()

        if val < self.min:
            old_min = self.min
            self.min = 2 * self.min - val
            return old_min
        
        return val
    
    def peek(self):
        if self.isEmpty():
            return None
        
        if self.s[-1] < self.min:
            return self.min
        
        return self.s[-1]


    def getMin(self) -> int:
        if self.isEmpty():
            return None
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()




