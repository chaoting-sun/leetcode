class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxDifference = -1
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                difference = nums[j] - nums[i]
                if difference > 0 and difference > maxDifference:
                    maxDifference = difference
        return maxDifference