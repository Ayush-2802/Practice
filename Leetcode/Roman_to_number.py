class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        roman = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        out = 0
        #method 1
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        
        for char in s:
            out += roman[char]
        return out

        #method 2
        prev = 0
        for i in s[::-1]:
            if roman[i] >= prev:
                out += roman[i]
            else:
                out -= roman[i]
            prev = roman[i]
        return out
