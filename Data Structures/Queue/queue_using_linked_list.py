# A linked list (LL) node 
# to store a queue entry 
class Node: 
      
    def __init__(self, data): 
        self.data = data 
        self.next = None
        
class MyQueue:
    
    def __init__(self):
        self.front = self.rear = None
    #Function to push an element into the queue.
    def push(self, item): 
        new = Node(item)
        if self.front == None:
            self.front = self.rear = new
            return
        self.rear.next = new
        self.rear = new
         #Add code here
    
    #Function to pop front element from the queue.
    def pop(self):
        if self.front==None:
            return -1
        temp = self.front
        self.front = self.front.next
        if self.front==None:
            self.rear = None
        return temp
         #add code here


#{ 
 # Driver Code Starts

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        s=MyQueue()
        q=int(input())
        q1=list(map(int,input().split()))
        i=0
        while(i<len(q1)):
            if(q1[i]==1):
                s.push(q1[i+1])
                i=i+2
            elif(q1[i]==2):
                print(s.pop(),end=" ")
                i=i+1
            elif(s.isEmpty()):
                print(-1)
                i=i+1
        print()   
        print("~")
# } Driver Code Ends