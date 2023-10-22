class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}
        def dfs(i, j):
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
        
        dfs(len(s)-1, len(t)-1)
        return cache[(len(s)-1, len(t)-1)]