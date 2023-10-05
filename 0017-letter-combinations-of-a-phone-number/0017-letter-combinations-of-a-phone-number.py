### method1: fill characters in order (mine)

# class Solution(object):
#     def letterCombinations(self, digits):
#         """
#         :type digits: str
#         :rtype: List[str]
#         """
#         if len(digits) == 0:
#             return []

#         d2e = {
#             '2': ['a', 'b', 'c'],
#             '3': ['d', 'e', 'f'],
#             '4': ['g', 'h', 'i'],
#             '5': ['j', 'k', 'l'],
#             '6': ['m', 'n', 'o'],
#             '7': ['p', 'q', 'r', 's'],
#             '8': ['t', 'u', 'v'],
#             '9': ['w', 'x', 'y', 'z']
#         }

#         combs = [d2e[d] for d in digits]
        
#         n_total_comb = 1
#         for c in combs:
#             n_total_comb *= len(c)
        
#         n_comb_each = []
#         n_curr_comb = n_total_comb
#         for c in combs:
#             n_curr_comb /= len(c)
#             n_comb_each.append(n_curr_comb)

#         ans = ['' for i in range(n_total_comb)]
        
#         for i in range(len(combs)):
#             s = ''
#             for j in range(len(combs[i])):
#                 s += combs[i][j] * n_comb_each[i]
#             total_s = s * (n_total_comb / len(s))

#             for k, s in enumerate(total_s):
#                 ans[k] += s

#         return ans


### method2: BFS

# class Solution(object):
#     def letterCombinations(self, digits):
#         """
#         :type digits: str
#         :rtype: List[str]
#         """
#         if len(digits) == 0:
#             return []

#         chars = ['', '', 'abc', 'def', 'ghi', 'jkl',
#                  'mno', 'pqrs', 'tuv', 'wxyz']
#         ans = ['']

#         for d in digits:
#             tmp = []
#             for a in ans:
#                 for e in chars[ord(d)-ord('0')]:
#                     tmp.append(a + e)
#             ans = tmp
#         return ans


# method3: DFS

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        chars = ['', '', 'abc', 'def', 'ghi', 'jkl',
                 'mno', 'pqrs', 'tuv','wxyz']

        def dfs(tmp, l, ans):
            if l == len(digits):
                ans.append(''.join(tmp))
                return
            
            for c in chars[ord(digits[l])-ord('0')]:
                tmp[l] = c
                dfs(tmp, l+1, ans)

        if len(digits) == 0:
            return []

        ans = []
        tmp = [''] * len(digits)
        dfs(tmp, 0, ans)

        return ans