class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rec = { 0: 0, 1: 0, 2: 0 }
        for i in range(len(nums)):
            rec[nums[i]] += 1

        for i in range(rec[0]):
            nums[i] = 0
        for i in range(rec[0], rec[0]+rec[1]):
            nums[i] = 1
        for i in range(rec[0]+rec[1], rec[0]+rec[1]+rec[2]):
            nums[i] = 2
        return nums