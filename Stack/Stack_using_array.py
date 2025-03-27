class stack:
    def __init__(self,cap):
        self.cap = cap
        self.top = -1
        self.arr = [0]*cap

    def IsFull(self):
        return self.top == self.cap - 1
    
    def IsEmpty(self):
        return self.top == -1
    
    def push(self,x):
        if self.IsFull():
            print("Overflow")
            return
        else:
            self.top+=1
            self.arr[self.top] = x
            return True
        
    def pop(self):
        if self.IsEmpty():
            print("Underflow")
            return
        else:
            temp = self.top
            self.top -= 1
            return temp
    
    def peek(self):
        if self.IsEmpty():
            print("Empty Stack")
            return
        else:
            return self.arr[self.top]
        
if __name__=="__main__":
    s = stack(3)
    s.push(10)
    s.push(20)
    s.push(30)

    print(f"Stack: {s.arr}")
    print(s.pop(), "popped from stack")
    print("Top element is:", s.peek())
    
    print("Elements present in stack:", end=" ")
    while not s.IsEmpty():
        print(s.peek(), end=" ")
        s.pop()