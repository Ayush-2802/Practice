class node:
    def __init__(self,data):
        self.data = data
        self.next = None

def NaiveMid(head): #time complexity of O(n^2)
    #first Pass
    temp = head
    c = 0
    while temp:
        c +=1
        temp = temp.next

    m = (c//2)+1

    #second Pass
    temp = head
    while temp:
        m -= 1
        if m == 0:
            break
        temp = temp.next

    return temp

def TortoiseAndHare(head):
    oddPtr = head
    evenPtr = head

    while oddPtr != None and oddPtr.next != None:
        evenPtr = evenPtr.next
        oddPtr = oddPtr.next.next

    return evenPtr

if __name__ == "__main__":
    head = node(10)
    head.next = node(20)
    head.next.next = node(30)
    head.next.next.next = node(40)

    head = TortoiseAndHare(head)
    print(head.data)