### method: dp

# source1: https://leetcode.com/problems/longest-common-subsequence/solutions/348884/c-with-picture-o-nm/?envType=list&envId=rr2ss0g5
# source2: https://emmielin.medium.com/leetcode-%E7%AD%86%E8%A8%98-1143-longest-common-subsequence-b6c7eebd1328

# time complexity: O(mn)
# space complexity: O(mn)

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]


### method: dp + optimized space

# time complexity: O(mn)
# space complexity: O(n)

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0 for _ in range(n+1)] for _ in range(2)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                curri = i % 2
                previ = 0 if curri == 1 else 1 
                if text1[i-1] == text2[j-1]:
                    dp[curri][j] = 1 + dp[previ][j-1]
                else:
                    dp[curri][j] = max(dp[previ][j], dp[curri][j-1])
        return dp[m%2][n]