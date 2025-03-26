class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

def LenList(head):
    l = 0
    t = head
    while t:
        l+=1
        t=t.next
    return l

if __name__ == "__main__":
    head = node(10)
    second = node(20)
    third = node(30)
    fourth = node(40)

    head.next = second
    second.prev = head
    second.next = third
    third.prev = second
    third.next = fourth
    fourth.prev = third

    length = LenList(head)
    print(f"Length of list : {length}")