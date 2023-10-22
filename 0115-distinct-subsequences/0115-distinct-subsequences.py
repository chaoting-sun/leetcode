### method1: dp (top to bottom)

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}
        def topToBottom(i, j):
            if j < 0: # has found all characters in t
                return 1
            elif i < 0: # has not found all characters in t
                return 0
            elif (i, j) in cache:
                return cache[(i, j)]

            if s[i] == t[j]:
                cache[(i, j)] = dfs(i-1, j-1) + dfs(i-1, j)
            else:
                cache[(i, j)] = dfs(i-1, j)
            return cache[(i, j)]
        
        topToBottom(len(s)-1, len(t)-1)
        return cache[(len(s)-1, len(t)-1)]


### method2: dp (bottom to top)

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = 1
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    """
                    if si == tj (s[i-1] == t[j-1]), we should consider two conds:
                    1. there may be k < i s.t. sk == tj. so we ignore si -> dp[i-1][j]
                    2. we match si and tj, and consider the combinations before
                    i and j -> dp[i-1][j-1]
                    """
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    """
                    si can be ignored, so we use the record dp[i-1][j]
                    """
                    dp[i][j] = dp[i-1][j]
        return dp[m][n]


### dp + space optimization: https://leetcode.com/problems/distinct-subsequences/solutions/2738744/recursion-to-dp-optimise-easy-understanding/?envType=list&envId=rr2ss0g5