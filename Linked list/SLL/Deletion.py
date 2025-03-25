class node:
    def __init__(self,data):
        self.data = data 
        self.next = None

class Deletion:
    def DelAtFront(head):
        if head is None:
            return None
        
        temp = head
        head = head.next
        del temp
        return head
    
    def DelAtLast(head):
        if not head:
            return None
        
        if not head.next:
            return Deletion.DelAtFront(head)
        
        sec = head
        while sec.next.next:
            sec = sec.next
        
        sec.next = None
        return head
    
    def DelAtPos(head,pos):
        if not head:
            return None
        
        # Case 1
        if pos == 1:
            return Deletion.DelAtFront(head)
        
        # Case 2
        temp = head
        prev = None
        for i in range(1,pos):
            prev = temp
            temp = temp.next
            if temp is None:
                print("Data Not Present")
                return head
        prev.next = temp.next
        return head

def PrintList(head):
    while head:
        print(head.data,end=" ")
        head = head.next

if __name__=="__main__":
    head = node(10)
    head.next = node(20)
    head.next.next = node(30)
    PrintList(head)
    print("")
    head = Deletion.DelAtPos(head,3)
    PrintList(head)