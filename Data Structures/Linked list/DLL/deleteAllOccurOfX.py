def deleteAllOccurOfX(self, head, x):
    if not head:
        return None
    
    while head and head.data == x:
        head = head.next
        if head:
            head.prev = None

    if not head:
        return None
    

    current = head
    while current.next:
        if current.next.data == x:
            if current.next.next:
                current.next = current.next.next
                current.next.prev = current
            else:
                current.next = None
        else:
            current = current.next
    
    return head