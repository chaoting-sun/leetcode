class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        firstMin = max(0, n-2*limit)
        firstMax = min(n, limit)

        ans = 0

        for i in range(firstMin, firstMax+1):
            secondMin = max(0, n-i-limit)
            secondMax = min(limit, n-i)
            ans += secondMax - secondMin + 1

        return ans