### method1: backtracking

# time complexity: O(2^n)
# space complexity: O(2^n)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, i, ans, subset):
            if i >= len(nums):
                ans.append(subset)
                return
            backtrack(nums, i+1, ans, subset) # don't take
            backtrack(nums, i+1, ans, subset+[nums[i]]) # take

        ans = []
        backtrack(nums, 0, ans, [])
        return ans


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, start, ans, subset):
            ans.append(subset)
            
            for i in range(start, len(nums)):
                backtrack(nums, i+1, ans, subset+[nums[i]])

        ans = []
        backtrack(nums, 0, ans, [])
        return ans


### method2: bit manipulation

# time complexity: O(n*2^n)
# space complexity: O(1)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(1<<len(nums)):
            subset = []
            for j in range(len(nums)):
                if (1<<j) & i:
                    subset.append(nums[j])
            ans.append(subset)
        return ans