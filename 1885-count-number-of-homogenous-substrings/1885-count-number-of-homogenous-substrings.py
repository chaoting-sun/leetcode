class Solution:
    def countContiguous(self, n, cache):
        if n in cache:
            return cache[n]
        cache[n] = (n+1)*n//2 % (10**9 + 7) 
        return cache[n]

    def countHomogenous(self, s: str) -> int:
        left = right = 0
        cache = {}
        number = 0

        while right < len(s):
            while right < len(s) and s[left] == s[right]:
                right += 1
            number += self.countContiguous(right-left, cache)
            left = right
        
        return number % (10**9 + 7)