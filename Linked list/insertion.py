class node:
    def __init__(self,data):
        self.data = data
        self.next = None

def InsertionAtFront(head,new_data):
    new = node(new_data)
    new.next = head
    return new

def InsertionAtEnd(head,new_data):
    new = node(new_data)
    if head is None:
        return new
    last = head
    while last.next:
        last = last.next

    last.next = new
    return head    

def printList(node):
    while node:
        print(node.data,end=" ")
        node = node.next

if __name__=="__main__":
    head = node(1)
    head.next = node(2)

    print("Original List: ",end="")
    printList(head)
    print("")

    new_data = 0
    head = InsertionAtFront(head,new_data)
    print("Updated after Insertion at Front: ",end="")
    printList(head)
    print("")

    new_data = 3
    head = InsertionAtEnd(head,new_data)
    print("Updated after Insertion at End: ",end="")
    printList(head)
    print("")
