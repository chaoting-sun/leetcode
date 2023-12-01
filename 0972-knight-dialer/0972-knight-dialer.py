# time complexity: O(n)
# space complexity: O(n)

class Solution:
    def knightDialer(self, n: int) -> int:
        jump = { 0: [4,6], 1: [6,8], 2: [7,9], 3: [4,8], 4: [0,3,9],
                 5: [], 6: [0,1,7], 7: [2,6], 8: [1,3], 9: [2,4]
                }
        
        dp = [[0]*n for _ in range(10)]
        for i in range(10):
            dp[i][0] = 1

        def backtrack(dp, d1, nLeft):
            if nLeft == 0:
                return 1

            if dp[d1][nLeft] != 0:
                return dp[d1][nLeft]

            for d2 in jump[d1]:
                dp[d1][nLeft] += backtrack(dp, d2, nLeft-1)
            return dp[d1][nLeft]

        ans = 0
        for d in range(10):
            ans += backtrack(dp, d, n-1)
            ans %= 10**9 + 7
        
        return ans