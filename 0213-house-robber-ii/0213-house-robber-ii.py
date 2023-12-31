class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        dp1 = [0] * len(nums) # House[0] - House[n-2]
        dp2 = [0] * len(nums) # House[1] - House[n-1]

        dp1[0] = nums[0] # steal
        dp1[1] = dp1[0] # cannot steal

        for i in range(2, len(nums)-1):
            dp1[i] = max(dp1[i-1], dp1[i-2]+nums[i])
        
        dp2[0] = 0
        dp2[1] = nums[1]

        for i in range(2, len(nums)):
            dp2[i] = max(dp2[i-1], dp2[i-2]+nums[i])

        return max(dp1[len(nums)-2], dp2[len(nums)-1])