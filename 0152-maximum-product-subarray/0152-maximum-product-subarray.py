### dp

# time complexity: O(N)
# space complexity: O(N)

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


### dp

# time complexity: O(N)
# space complexity: O(N)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        global_max = local_min = local_max = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                local_max, local_min = local_min, local_max
            
            local_max = max(local_max*nums[i], nums[i])
            local_min = min(local_min*nums[i], nums[i])
            global_max = max(local_max, global_max)
        return global_max