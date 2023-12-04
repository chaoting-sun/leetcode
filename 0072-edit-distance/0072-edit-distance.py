### method1: recursion (TLE)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def recursion(i, j):
            if i == len(word1) and j == len(word2):
                return 0
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            
            if word1[i] == word2[j]:
                return recursion(i+1, j+1)
            else:
                cnt_insert = 1 + recursion(i, j+1)
                cnt_delete = 1 + recursion(i+1, j)
                cnt_replace = 1 + recursion(i+1, j+1)
                return min(cnt_insert, cnt_delete, cnt_replace)

        return recursion(0, 0)


### method2: recursion + memory

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def recursion(i, j, mem):
            if i == len(word1) and j == len(word2):
                return 0
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            
            if (i, j) in mem:
                return mem[(i, j)]

            if word1[i] == word2[j]:
                cnt = recursion(i+1, j+1, mem)
            else:
                cnt_insert = 1 + recursion(i, j+1, mem)
                cnt_delete = 1 + recursion(i+1, j, mem)
                cnt_replace = 1 + recursion(i+1, j+1, mem)
                cnt = min(cnt_insert, cnt_delete, cnt_replace)
            mem[(i, j)] = cnt
            return cnt

        mem = {}
        return recursion(0, 0, mem)