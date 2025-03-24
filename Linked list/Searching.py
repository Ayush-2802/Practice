class node:
    def __init__(self,data):
        self.data = data
        self.next = None

def search(head,x):
    cur  = head
    while cur is not None:
        if cur.data ==  x:
            return True
        cur = cur.next
    return False

if __name__=="__main__":
    head = node(10)
    head.next = node(20)
    head.next.next = node(30)
    head.next.next.next = node(20)
    x = 30

    if search(head,x):
        print("yes")
    else: 
        print("No")