class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_pos = {}
        l = 0
        max_length = 0
        
        for r, char in enumerate(s):
            if char in char_pos and char_pos[char] >= l:
                l = char_pos[char] + 1
            else:
                max_length = max(max_length, r - l + 1)
            char_pos[char] = r
            
        return max_length

# Fix the function call
s = "abcabcbb"
solution = Solution()
print(solution.lengthOfLongestSubstring(s))