class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class traversal:
    def NaiveListReversal(head):
        temp = head
        st = []
        
        # 1st pass
        while temp:
            st.append(temp.data)
            temp = temp.next

        #2nd Pass
        temp = head
        while temp:
            temp.data = st[-1] #stack.top
            st.pop()
            temp = temp.next
        return head

    def OptimizedListReversal(head):
        temp = head
        prev = None

        while temp:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front

        return prev
    
class Recursion:
    def RecRev(head):
        if not head or not head.next:
            return head
        new = Recursion.RecRev(head.next)
        front = head.next
        front.next = head
        head.next = None
        return new

def printList(head):
    while head:
        print(head.data,end=" ")
        head = head.next
    print()

if __name__=="__main__":
    head = node(10)
    head.next = node(20)
    head.next.next = node(30)
    head.next.next.next = node(40)

    # head = traversal.OptimizedListReversal(head)
    head = Recursion.RecRev(head)
    printList(head)