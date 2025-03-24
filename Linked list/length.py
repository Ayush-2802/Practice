class node:
    def __init__(self,data):
        self.data = data
        self.next = None

def lenList(head):
    l = 0
    c = head
    while c is not None:
        l += 1
        c = c.next
    return l

if __name__=="__main__":
    head = node(1)
    head.next = node(2)
    head.next.next = node(3)
    head.next.next.next = node(4)

    print(lenList(head)) #4