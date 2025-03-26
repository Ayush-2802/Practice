class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

def printList(head):
    temp = head
    while temp:
        print(temp.data,end=" ")
        temp = temp.next
    print()

class deletion:
    def Front(head):
        if head is None: 
            return None
        temp = head
        new_head = head.next
        if new_head!=None:
            new_head.prev = None

        del temp
        return new_head
    
    def End(head):
        if head is None or head.next is None:
            return None

        temp = head
        while temp.next is not None:
            temp = temp.next
        
        if temp.prev is not None:
            temp.prev.next = None
        
        return head
    
    def Pos(head,pos):
        if head == None:
            return None
        temp = head
        for i in range(1,pos-1):
            if temp is None:
                print("out of bount")
                return head
            temp = temp.next
        
        if temp.prev != None:
            temp.prev.next = temp.next

        if temp.next != None:
            temp.next.prev = temp.prev
        
        if head == temp:
            head = temp.next
        
        del temp
        return head

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

    head = deletion.Front(head)
    head = deletion.End(head)
    head = deletion.Pos(head,2)
    
    print("After Insertion: ",end = "")
    printList(head)

    def pos(head,pos):
        if head == None:
            return None
        
        temp = head
        for _ in range(1,pos-1):
            if temp is None:
                return head #out of bound
            temp = temp.next

        if temp.prev != None:
            temp.prev.next = temp.next

        if temp.next != None:
            temp.next.prev = temp.prev

        if temp == head:
            head = temp.next

        del temp
        return head
    