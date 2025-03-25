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