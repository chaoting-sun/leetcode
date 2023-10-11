### method1:  dfs

# every time we check if s[start:i] is in wordDict, as well as s[i+1:] in the next loop

# time complexity: O(2^N) (https://leetcode.com/problems/word-break/solutions/169383/The-Time-Complexity-of-The-Brute-Force-Method-Should-Be-O(2n)-and-Prove-It-Below/)
# space complexity: (N)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        size = len(s)
        memory = [-1] * size
        wordSet = set(wordDict)

        def isValid(start):
            if start >= size: return True
            if memory[start] != -1: return memory[start]

            for i in range(start+1, size+1):
                if s[start:i] in wordSet and isValid(i): # found a valid combination of words
                    memory[start] = 1
                    return 1
            memory[start] = 0
            return 0

        valid = isValid(0)
        return valid == 1


### dp

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        size = len(s)
        wordSet = set(wordDict)
        dp = [0] * (len(s) + 1) # dp[i]: if 1, then s[:i] is valid
        dp[0] = 1

        for i in range(size+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = 1
                    break
        return dp[size]


### bfs

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        sSize = len(s)

        q = [0]
        visited = [0] * len(s)

        while q:
            qSize = len(q)

            for i in range(qSize):
                start = q.pop(0)
                if visited[start]:
                    continue

                for i in range(start+1, sSize+1):
                    if s[start:i] in wordSet:
                        if i == sSize:
                            return True
                        q.append(i)
                visited[start] = 1
        return False

# nice source: https://www.cnblogs.com/grandyang/p/4257740.html