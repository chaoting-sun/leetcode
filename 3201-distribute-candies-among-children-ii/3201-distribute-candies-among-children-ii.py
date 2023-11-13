### method1

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


### method2

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        if n > 3*limit:
            return 0

        ans = 0
        for i in range(min(n, limit)+1):
            nLeft = n-i
            if nLeft > 2*limit:
                continue
            # By default, there are left+1 ways to split among 2nd and 3rd
            # But 2*(left-limit) will be invalid
            if nLeft <= limit:
                ans += nLeft+1
            else:
                ans += nLeft+1-2*(nLeft-limit)
        return ans