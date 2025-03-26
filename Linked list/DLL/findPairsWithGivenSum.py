class Solution:
    def findPairsWithGivenSum(self, target : int, head : Optional['Node']) -> List[List[int]]:
        # code here
        left = head
        right = head
        while right.next:
            right = right.next

        st = []
            
        while left.data < right.data:
            if left.data+right.data == target:
                st.append([left.data,right.data])
                left = left.next
                right = right.prev
            elif left.data + right.data < target:
                left = left.next
            else:
                right = right.prev

        return st
