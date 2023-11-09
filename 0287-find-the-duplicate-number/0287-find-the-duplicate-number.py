### method: sort

# time complexity: O(NlogN)
# space complexity: O(1)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i] == 0:
                return nums[i]
        return -1