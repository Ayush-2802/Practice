def getIntersectionNode(headA,headB):
    t1 = headA
    t2 = headB

    while t1!=t2:
        if t1 is None:
            t1 = headB
        else:
            t1 = t1.next

        if t2 is None:
            t2 = headA
        else:
            t2 = t2.next
        
        if t1 is None and t2 is None:
             return None
        
        return t1