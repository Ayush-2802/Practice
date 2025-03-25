# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        temp = dummy
        carry = 0
        t1 = l1
        t2 = l2

        while t1!=None or t2!=None:
            sum = carry
            if t1: sum += t1.val
            if t2: sum += t2.val
            new = ListNode(sum%10)
            carry = sum//10

            temp.next = new
            temp=temp.next

            if t1: t1 = t1.next
            if t2: t2 = t2.next

        if carry:
            new = ListNode(carry)
            temp.next = new
        
        return dummy.next

            
            
        