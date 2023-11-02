### method1: backtracking (TLE)

class Solution:
    def rob(self, nums: List[int]) -> int:
        maxAmount = 0
        
        def backtrack(nums, i, lastChoice, accSum):
            nonlocal maxAmount
            if i == len(nums):
                maxAmount = max(maxAmount, accSum)
                return
            
            if lastChoice == 1:
                backtrack(nums, i+1, 0, accSum)
            else:
                backtrack(nums, i+1, 0, accSum)
                backtrack(nums, i+1, 1, accSum+nums[i])

        backtrack(nums, 0, 0, 0)
        return maxAmount


### method1: backtracking (TLE)

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        maxNotChosen = [0] * (1+n)
        maxChosen = [0] * (1+n)

        for i in range(1, n+1):
            maxChosen[i] = maxNotChosen[i-1] + nums[i-1]
            maxNotChosen[i] = max(maxChosen[i-1], maxNotChosen[i-1])
        return max(maxChosen[n], maxNotChosen[n])