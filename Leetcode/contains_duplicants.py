class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # method 1 hash set
        dupli = set()

        for i in nums:
            if i in dupli:
                return True
            dupli.add(i)
        else:
            return False

        # method 2
        #uses set to check for duplicates
        #if there are duplicates, the length of the set will be less than the length of the list
        #if there are no duplicates, the length of the set will be equal to the length of the list
        #return True if there are duplicates, False if there are no duplicates
        return len(nums) != len(set(nums))


nums = [2,14,18,22,22]
print(Solution().containsDuplicate(nums))
