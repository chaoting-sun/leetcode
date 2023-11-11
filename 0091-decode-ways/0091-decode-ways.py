### method1: backtracking

class Solution:
    def backtrack(self, i, s, cnt):
        if i == len(s):
            return cnt + 1
        
        if s[i] != '0':
            cnt = self.backtrack(i+1, s, cnt)
            if i < len(s)-1 and int(s[i:i+2]) <= 26:
                cnt = self.backtrack(i+2, s, cnt)
        return cnt
    
    
    def numDecodings(self, s: str) -> int:
        return self.backtrack(0, s, 0)


### method2: backtracking + memory

class Solution:
    def backtrack(self, i, s, memory):
        # invalid condition
        if i < len(s) and s[i] == '0':
            return 0
        
        # finish condition
        if i == len(s):
            return 1

        # return the memorized value

        if memory[i] != -1:
            return memory[i]

        cnt = 0
        if s[i] == '0':
            return 0
        
        cnt = self.backtrack(i+1, s, memory)
        if i < len(s)-1 and int(s[i:i+2]) <= 26:
            cnt += self.backtrack(i+2, s, memory)
        memory[i] = cnt

        return memory[i]
    
    def numDecodings(self, s: str) -> int:
        memory = [-1] * len(s)
        return self.backtrack(0, s, memory)


# ### method2: dp

# class Solution:
#     def numDecodings(self, s: str) -> int:
#         """
#         if s[i] != '0':
#             dp[i] = dp[i-1]
#         if int(s[i-1:i+1]) <= 26:
#             dp[i] += dp[i-2]
#         """

#         if s[0] == '0':
#             return 0
#         dp = [0] * (len(s)+1)
#         dp[1] = 1

#         for i in range(1, len(s)):
#             if int(s[i-1:i+1]) <= 26:
#                 dp[i+1] += dp[i-1] if i > 1 else 1
#             if s[i] != '0':
#                 dp[i+1] += dp[i]
#             if dp[i+1] == 0:
#                 return 0

#         print(dp)
#         return dp[len(s)]

# '''
# dp = [0 1 2 0 0]
# s  =   [2 1 0 1]


# dp = [1 1 1]
# s    = [6 0]
# '''