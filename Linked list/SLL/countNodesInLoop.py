class Solution:
    # Function to find the length of a loop in the linked list.
    def findLen(self,slow,fast):
        l = 0
        fast = fast.next
        while slow!=fast:
            l+=1
            fast = fast.next
        return l
    
    def countNodesInLoop(self, head):
        #Your code here
        slow = head
        fast = head
        
        while fast!=None and fast.next!=None:
            slow = slow.next
            fast = fast.next
            
            if slow == fast:
                return self.findLen(slow,fast)
        return 0