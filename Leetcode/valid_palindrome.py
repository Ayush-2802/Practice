class Solution:
    def isPalindrome(self, s: str) -> bool:

        new = ''.join([i for i in s[::-1] if i.isalnum()])
        s = ''.join([i for i in s if i.isalnum()])
        if new.lower() == s.lower():
            return True
        else:
            return False

        # method 2
    def myAlnum(self,c):
        return (ord("A") <= ord(c) <= ord('Z') or 
                ord("a") <= ord(c) <= ord('z') or
                ord("0") <= ord(c) <= ord('9'))
    
    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s)-1
        while l < r:
            while l<r and not self.myAlnum(s[l]):
                l +=1
            while r>l and not self.myAlnum(s[r]):
                r -=1
            if s[l].lower() != s[r].lower():
                return False
            l,r = l+1,r-1
        return True
