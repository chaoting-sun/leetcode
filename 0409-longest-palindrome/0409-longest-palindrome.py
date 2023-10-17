class Solution:
    def longestPalindrome(self, s: str) -> int:
        m = defaultdict(int)
        for ch in s:
            m[ch] += 1
        
        hasOdd = False
        length = 0

        for k, v in m.items():
            if v % 2 == 0:
                length += v
            else:
                length += v - 1
                hasOdd = True  

        return length + 1 if hasOdd else length