### method1: two-pass algorithm

# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         rec = { 0: 0, 1: 0, 2: 0 }
#         for i in range(len(nums)):
#             rec[nums[i]] += 1

#         for i in range(rec[0]):
#             nums[i] = 0
#         for i in range(rec[0], rec[0]+rec[1]):
#             nums[i] = 1
#             for i in range(rec[0]+rec[1], rec[0]+rec[1]+rec[2]):
#                 nums[i] = 2
#             return nums


### method2: one-pass algorithm (Dutch National Flag Algorithm)

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low, mid, high = 0, 0, len(nums)-1
        
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
            else:
                mid += 1
        return nums
