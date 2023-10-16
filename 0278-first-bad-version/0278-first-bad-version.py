# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def binarySearch(self, l, r):
        c = int((l + r) // 2)
        if isBadVersion(c):
            if c == 1 or not isBadVersion(c-1):
                return c
            return self.binarySearch(l ,c)
        else:
            return self.binarySearch(c, r)
    
    def firstBadVersion(self, n: int) -> int:
        return self.binarySearch(1, n+1)