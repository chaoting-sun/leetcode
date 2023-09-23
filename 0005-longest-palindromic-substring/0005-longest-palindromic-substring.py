### method1: two stacks

# class Solution(object):
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         stk1 = []
#         stk2 = []
#         curr = right = 0
#         max_len = 1
#         ans = s[0]

#         while curr < len(s):
#             # even
#             if len(stk1) >= 1 and stk1[-1] == s[curr]:
#                 right = curr
#                 while len(stk1) and right < len(s) and stk1[-1] == s[right]:
#                     stk2.append(stk1.pop(-1))
#                     right += 1

#                 curr_len = 2 * (right - curr)
#                 if curr_len > max_len:
#                     max_len = curr_len
#                     ans = s[len(stk1):right]

#                 while len(stk2):
#                     stk1.append(stk2.pop(-1))

#             # odd
#             if len(stk1) >= 2 and stk1[-2] == s[curr]:
#                 right = curr
#                 stk2.append(stk1.pop(-1))
#                 while len(stk1) and right < len(s) and stk1[-1] == s[right]:
#                     stk2.append(stk1.pop(-1))
#                     right += 1

#                 curr_len = 2 * (right - curr) + 1
#                 if curr_len > max_len:
#                     max_len = curr_len
#                     ans = s[len(stk1):right]

#                 while len(stk2):
#                     stk1.append(stk2.pop(-1))

#             stk1.append(s[curr])
#             curr += 1

#         return ans


### method2: expand around center (EAC)

class Solution(object):
    def substr(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return l, r

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s
        
        ans = ""
        max_len = 0

        for i in range(len(s)-1):
            # odd
            odd_l, odd_r = self.substr(s, i, i)
            if max_len < odd_r - odd_l - 1:
                max_len = odd_r - odd_l - 1
                ans = s[odd_l+1:odd_r]

            # even
            even_l, even_r = self.substr(s, i, i+1)
            if max_len < even_r - even_l - 1:
                max_len = even_r - even_l - 1
                ans = s[even_l+1:even_r]
        
        return ans


### method3: dynamic programming (TLE)

# import numpy as np

# class Solution(object):
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         ans = s[0]
#         max_len = 1
#         dp = np.ones((len(s), len(s))) # default: True
        
#         for j in range(len(s)):
#             for i in range(j):
#                 if i + 1 == j and s[i] != s[j]:
#                     dp[i][j] = 0

#                 if dp[i+1][j-1] == 0 or s[i] != s[j]:
#                     dp[i][j] = 0

#                 if dp[i][j] == 1 and j - i + 1 > max_len:
#                     max_len = j - i + 1
#                     ans = s[i:j+1]            
#         return ans


# method4: dynamic programming (TLE)

# import numpy as np

# class Solution(object):
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         ans = s[0]
#         max_len = 1
#         dp = np.ones((len(s), len(s))) # default: True
        
#         for j in range(len(s)):
#             for i in range(j):
#                 if i + 1 == j and s[i] != s[j]:
#                     dp[i][j] = 0

#                 if dp[i+1][j-1] == 0 or s[i] != s[j]:
#                     dp[i][j] = 0

#                 if dp[i][j] == 1 and j - i + 1 > max_len:
#                     max_len = j - i + 1
#                     ans = s[i:j+1]            
#         return ans


### method5: Manacher algorithm (Time complexity = O(N))
# too hard