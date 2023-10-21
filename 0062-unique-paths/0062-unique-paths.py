### method1: dfs (O(2^{n+m}); TLE)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dfs(i, j):
            if i >= m or j >= n:
                return 0
            if i == m-1 and j == n-1:
                return 1
            return dfs(i+1, j) + dfs(i, j+1)

        return dfs(0, 0)


### method2: dp

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * n] * m
        dp[0][0] = 0
        for i in range(m):
            dp[i][0] = 1
        for i in range(n):
            dp[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

        