# class Solution:
#     def maximumDifference(self, nums: List[int]) -> int:
#         max_difference = -1
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 difference = nums[j] - nums[i]
#                 if difference > 0 and difference > max_difference:
#                     max_difference = difference
#         return max_difference

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_difference = -1
        for divide_index in range(1, len(nums)):
            left_sorted = sorted(nums[0:divide_index])
            right_sorted = sorted(nums[divide_index: len(nums)])
            if len(left_sorted) > 0 and len(right_sorted) > 0:
                difference = right_sorted[len(right_sorted)-1] - left_sorted[0]
                if difference > 0 and difference > max_difference:
                    max_difference = difference
        return max_difference