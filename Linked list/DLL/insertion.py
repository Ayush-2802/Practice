class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class insert:
    def Front(head,data):
        new = node(data)
        new.next = head

        if head != None:
            head.prev = new

        return new
    
    def End(head,data):
        new = node(data)
        if head is None:
            head = new
        else:
            temp = head
            while temp.next is not None:
                temp = temp.next
            
            temp.next = new
            new.prev = temp
        
            return head
    def Pos(head,data,pos):
        new = node(data)
        if pos == 1:
            insert.Front(head,data)
        temp = head
        for i in range(1,pos-1):
            if temp is None:
                print("out of bound")
                return head
            temp = temp.next
        
        if temp is None:
            insert.End(head,data)
            return head
        
        new.next = temp.next
        new.prev = temp
        temp.next = new

        if new.next is not None:
            new.next.prev = new
        return head
    
def printList(head):
    temp = head
    while temp:
        print(temp.data,end=" ")
        temp = temp.next
    print()

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

    print("Before Insertion: ",end = "")
    printList(head)

    head = insert.Front(head,1)
    head = insert.End(head,1)
    head = insert.Pos(head,1,4)
    
    print("After Insertion: ",end = "")
    printList(head)