class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        dum = ListNode(0)
        dum.next = head
        temp = head
        c=0
        while temp:
            c+=1
            temp=temp.next

        s = c-n
        temp = dum

        temp = dum
        for i in range(s):
            temp = temp.next

        temp.next = temp.next.next if temp.next else None
        return dum.next
    
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head

        for i in range(n): fast = fast.next
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        
        d = slow.next
        slow.next = slow.next.next
        del d
        return head