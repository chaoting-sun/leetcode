class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxP = [0] * len(nums)
        minP = [0] * len(nums)

        res = maxP[0] = minP[0] = nums[0]

        for i in range(1, len(nums)):
            maxP[i] = max(maxP[i-1]*nums[i], minP[i-1]*nums[i], nums[i])
            minP[i] = min(maxP[i-1]*nums[i], minP[i-1]*nums[i], nums[i])
            res = max(res, maxP[i])
        return res