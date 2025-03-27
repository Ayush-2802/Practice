class node:
    def __init__(self,data):
        self.data = data
        self .next = None

def BruteSort(head):
    s = []
    temp = head
    while temp:
        s.append(temp.data)
        temp = temp.next

    s.sort()
    temp = head
    i = 0 
    while temp:
        temp.data = s[i]
        i += 1
        temp = temp.next

    return head

def findMid(head):
    slow = head
    fast = head.next

    while fast!=None and fast.next!=None:
        slow = slow.next
        fast = fast.next.next

    return slow

def merge(leftHead,rightHead):
    dum = node(0)
    temp = dum

    while leftHead != None and rightHead != None:
        if leftHead.data < rightHead.data:
            temp.next = leftHead
            temp = leftHead
            leftHead = leftHead.next

        else:
            temp.next = rightHead
            temp = rightHead
            rightHead = rightHead.next
            
    if leftHead : temp.next = leftHead
    else: temp.next = rightHead

    return dum.next


def MergeSort(head):
    if head == None or head.next == None:
        return head
    
    mid = findMid(head)
    leftHead = head 
    righthead = mid.next
    mid.next = None

    leftHead = MergeSort(leftHead)
    righthead = MergeSort(righthead)

    return merge(leftHead,righthead)

def printList(head):
    temp = head
    while temp:
        print(temp.data,end=" ")
        temp = temp.next
    print()

if __name__=="__main__":
    head = node(1)
    head.next = node(50)
    head.next.next= node(2)
    head.next.next.next = node(7)

    head = MergeSort(head)
    printList(head)