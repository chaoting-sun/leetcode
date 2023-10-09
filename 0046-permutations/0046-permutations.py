### method1: dfs

class Solution:
    def dfs(self, prevNums, maxL, prevSet, ans):
        if len(prevSet) == maxL:
            ans.append(prevSet)
            return
        
        for i in range(len(prevNums)):
            curSet = prevSet + [prevNums[i]]
            curNums = prevNums[:i] + prevNums[i+1:]
            self.dfs(curNums, maxL, curSet, ans)
            
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.dfs(nums, len(nums), [], ans)
        return ans

### nice source:
# https://leetcode.com/problems/permutations/solutions/18239/a-general-approach-to-backtracking-questions-in-java-subsets-permutations-combination-sum-palindrome-partioning/?envType=list&envId=rab78cw1