# method1: backtracking; dfs

class Solution:
    def backtrack(self, nums, start, prevSub, subs):
        subs.append(prevSub)

        for i in range(start, len(nums)):
            currSub = prevSub + [nums[i]]
            self.backtrack(nums, i+1, currSub, subs)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        subs = []

        self.backtrack(nums, 0, [], subs)
        return subs