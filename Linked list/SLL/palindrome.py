class node:
    def __init__(self,val):
        self.val = val
        self.next = None

def reverse(head):
    temp = head
    prev = None

    while temp:
        front = temp.next
        temp.next = prev
        prev = temp
        temp = front

    return prev

def isPalindrome(head):
    # Edge case: empty list or single node
    if not head or not head.next:
        return True
    
    # Find the middle
    slow = fast = head
    while fast.next and fast.next.next:  # Modified condition for proper middle
        slow = slow.next
        fast = fast.next.next
    
    # Reverse the second half
    second_half = reverse(slow.next)
    
    # Compare first half with reversed second half
    first = head
    second = second_half
    
    result = True
    while second:  # Loop until end of second (shorter) half
        if first.val != second.val:
            result = False
            break
        first = first.next
        second = second.next
    
    # Restore the linked list (optional, but good practice)
    slow.next = reverse(second_half)
    
    return result

if __name__=="__main__":
    # Example 1: Palindrome (1->2->2->1)
    head = node(1)
    head.next = node(2)
    head.next.next = node(2)
    head.next.next.next = node(1)

    if isPalindrome(head):
        print("True")  # Should print True
    else:
        print("False")
        
    # Example 2: Not Palindrome (1->2->3->4)
    head2 = node(1)
    head2.next = node(2)
    head2.next.next = node(3)
    head2.next.next.next = node(4)
    
    if isPalindrome(head2):
        print("True")
    else:
        print("False")  # Should print False