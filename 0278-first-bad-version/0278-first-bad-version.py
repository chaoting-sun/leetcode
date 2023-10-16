# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def binarySearch(self, l, r):
        c = int(l + (r - l) / 2)
        if isBadVersion(c):
            if c == 1 or not isBadVersion(c-1):
                return c
            return self.binarySearch(l ,c)
        else:
            return self.binarySearch(c, r)
    
    def firstBadVersion(self, n: int) -> int:
        return self.binarySearch(1, n+1)


### source: https://leetcode.com/problems/first-bad-version/solutions/1591935/python-solution-easy-to-understand-binary-search-with-detailed-explanation/?envType=list&envId=rab78cw1

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n

        while l < r:
            mid = l + (r-l)//2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        return l