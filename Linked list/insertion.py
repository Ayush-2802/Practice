class node:
    def __init__(self,data):
        self.data = data
        self.next = None

def InsertionAtFront(head,new_data):
    new = node(new_data)
    new.next = head
    return new

def InsertionAtEnd():
    pass

def printList(head):
    c = head
    while c is not None:
        print(c.data,end=" ")
        c = c.next
    print()

if __name__=="__main__":
    head = node(1)
    head.next = node(2)

    print("Original List: ",end="")
    printList(head)

    new_data = 0
    head = InsertionAtFront(head,new_data)
    print("Updated after Front Insertion: ",end="")
    printList(head)