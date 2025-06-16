# class Solution:
#     def maximumDifference(self, nums: List[int]) -> int:
#         max_difference = -1
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 difference = nums[j] - nums[i]
#                 if difference > 0 and difference > max_difference:
#                     max_difference = difference
#         return max_difference

# class Solution:
#     def maximumDifference(self, nums: List[int]) -> int:
#         max_difference = -1
#         for divide_index in range(1, len(nums)):
#             left_sorted = sorted(nums[0:divide_index])
#             right_sorted = sorted(nums[divide_index: len(nums)])
#             if len(left_sorted) > 0 and len(right_sorted) > 0:
#                 difference = right_sorted[len(right_sorted)-1] - left_sorted[0]
#                 if difference > 0 and difference > max_difference:
#                     max_difference = difference
#         return max_difference

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        prefix_min, suffix_max = nums[:], nums[:]
        
        current_min = nums[0]
        for i in range(len(nums)):
            if nums[i] < current_min:
                current_min = nums[i]
                prefix_min[i] = nums[i]
            else:
                prefix_min[i] = current_min

        current_max = nums[len(nums)-1]
        for i in range(len(nums)-1, -1, -1):
            if nums[i] > current_max:
                current_max = nums[i]
                suffix_max[i] = nums[i]
            else:
                suffix_max[i] = current_max

        max_difference = -1
        for i in range(len(nums)):
            difference = suffix_max[i] - prefix_min[i]
            if difference > 0 and difference > max_difference:
                max_difference = difference
        return max_difference