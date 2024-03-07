### backtracking

class Solution(object):
    def backtrack(self, ans, candidates, l, r, prevSet, prevLeft):
        if prevLeft == 0:
            ans.append(prevSet)
            return
        if prevLeft < 0:
            return
        
        for i in range(l, r + 1):
            if candidates[i] <= prevLeft:
                currSet = prevSet + [candidates[i]]
                currLeft = prevLeft - candidates[i]
                self.backtrack(ans, candidates, i, r, currSet, currLeft)
            else:
                break

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        l, r = 0, len(candidates)-1
        candidates.sort()
        while r > 0 and candidates[r] > target:
            r -= 1

        self.backtrack(ans, candidates, l, r, [], target)
        return ans


### dp

# source: https://leetcode.com/problems/combination-sum/solutions/937255/python-3-dfs-backtracking-two-dp-methods-explanations

class Solution(object):
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target+1)]
        for c in candidates:                                  # O(N): for each candidate
            for i in range(c, target+1):                      # O(M): for each possible value <= target
                if i == c: dp[i].append([c])
                for comb in dp[i-c]: dp[i].append(comb + [c]) # O(M) worst: for each combination
        return dp[-1]
