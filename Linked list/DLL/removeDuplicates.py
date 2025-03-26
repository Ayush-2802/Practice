class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        # code here
        # return head after editing list
        temp = head
        while temp and temp.next:
            if temp.next.data == temp.data:
                
                dupli = temp.next
                temp.next = dupli.next

                if dupli.next:
                    dupli.next.prev = temp
            
            else:
                temp = temp.next
            
        return head