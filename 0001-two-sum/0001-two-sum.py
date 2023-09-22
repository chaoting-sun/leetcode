### method1: Brute force

# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         for i in range(len(nums)-1):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#         return []


### method2: argsort

# import numpy as np

# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         i = 0
#         j = len(nums) - 1

#         nums = np.array(nums)
#         ids = np.argsort(nums)
#         nums = nums[ids] # sort

#         while i < j:
#             if nums[i] + nums[j] == target:
#                 return [ids[i], ids[j]]
#             elif nums[i] + nums[j] < target:
#                 i += 1
#             elif nums[i] + nums[j] > target:
#                 j -= 1
#         return []


### method3: hash table

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_table = { nums[i]: i for i in range(len(nums)) }
        for i in range(len(nums)):
            left = target - nums[i]
            if left in hash_table and hash_table[left] != i:
                return [i, hash_table[left]]
        return []