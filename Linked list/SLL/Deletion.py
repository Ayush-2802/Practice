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
    head = Deletion.DelAtFront(head)
    PrintList(head)