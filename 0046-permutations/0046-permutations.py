### method1: dfs

class Solution:
    def dfs(self, size, prevNums, subset, ans):
        if len(subset) == size:
            ans.append(subset)
            return
        
        for i in range(len(prevNums)):
            curSubset = subset + [prevNums[i]]
            curNums = prevNums[:i] + prevNums[i+1:]
            self.dfs(size, curNums, curSubset, ans)

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.dfs(len(nums), nums, [], ans)
        return ans


### nice source:
# https://leetcode.com/problems/permutations/solutions/18239/a-general-approach-to-backtracking-questions-in-java-subsets-permutations-combination-sum-palindrome-partioning/?envType=list&envId=rab78cw1