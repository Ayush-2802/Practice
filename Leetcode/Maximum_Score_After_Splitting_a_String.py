class Solution:
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_score = 0
        for i in range(1, len(s)):
            left = s[:i]
            right = s[i:]
            score = left.count('0') + right.count('1')
            max_score = max(max_score, score)

        return max_score

s = "00111"
solution = Solution()
print(solution.maxScore(s))
