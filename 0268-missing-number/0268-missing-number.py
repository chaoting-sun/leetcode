### method: sort + iteration

# time complexity: O(NlogN)
# space complexity: O(1)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        if nums[0] != 0: return 0
        if nums[len(nums)-1] != len(nums): return len(nums)

        for i in range(0, len(nums)-1):
            if nums[i+1]-nums[i] == 2:
                return nums[i]+1

        return -1


### method: record existence

# time complexity: O(N)
# space complexity: O(N)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        existed = [0] * (len(nums)+1)
        for n in nums:
            existed[n] = 1
        for i, e in enumerate(existed):
            if e == 0:
                return i
        return -1


### method:

# time complexity: O(N)
# space complexity: O(1)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        totalsum = (1 + len(nums)) * len(nums) // 2
        for n in nums:
            totalsum -= n
        return totalsum