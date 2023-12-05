class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, i, ans, subset):
            if i >= len(nums):
                ans.append(subset)
                return
            backtrack(nums, i+1, ans, subset)
            backtrack(nums, i+1, ans, subset+[nums[i]])

        ans = []
        backtrack(nums, 0, ans, [])
        return ans