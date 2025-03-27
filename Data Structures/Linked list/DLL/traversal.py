class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

def ForwardTraversal(head):
    temp = head
    while temp:
        print(temp.data,end=" ")
        temp = temp.next

    print()

def ForwardTraversalRec(head):
    if head is None:
        return 
    print(head.data,end=" ")
    ForwardTraversalRec(head.next)

def BackwardTraversal(tail):
    temp = tail
    while temp:
        print(temp.data,end=" ")
        temp = temp.prev
    print()

def BackwardTraversalRec(tail):
    if tail is None:
        return
    print(tail.data,end=" ")
    BackwardTraversalRec(tail.next)

if __name__ == "__main__":
    head = node(10)
    second = node(20)
    third = node(30)

    head.next = second
    second.prev = head
    second.next = third
    third.prev = second

    print("Forward Traversal :",end = "")
    ForwardTraversal(head)

    print("Backward Traversal :",end = "")
    BackwardTraversal(third)