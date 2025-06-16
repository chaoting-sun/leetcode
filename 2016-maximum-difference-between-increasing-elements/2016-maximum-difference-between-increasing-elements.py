# --- Brute-force search -------------------------------------------------
# Time complexity:  O(n^2)
# Space complexity: O(1)
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_difference = -1
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                difference = nums[j] - nums[i]
                if difference > 0 and difference > max_difference:
                    max_difference = difference
        return max_difference

# --- Sort left and right partitions ------------------------------------
# Time complexity:  O(n log n)
# Space complexity: O(n)
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_difference = -1
        for split in range(1, len(nums)):
            left_sorted = sorted(nums[0:split])
            right_sorted = sorted(nums[split: len(nums)])
            if len(left_sorted) > 0 and len(right_sorted) > 0:
                difference = right_sorted[len(right_sorted)-1] - left_sorted[0]
                if difference > 0 and difference > max_difference:
                    max_difference = difference
        return max_difference

# --- Prefix-minimum and suffix-maximum arrays --------------------------
# Time complexity:  O(n)
# Space complexity: O(n)
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

# --- Single pass with running minimum ----------------------------------
# Time complexity:  O(n)
# Space complexity: O(1)

# Idea:  If there exists i < j with nums[i] < nums[j], the maximum
#        difference is captured by scanning left-to-right while keeping
#        the smallest value seen so far and updating the answer on the fly.
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        premin = nums[0]
        max_difference = -1
        for i in range(1, len(nums)):
            if nums[i] > premin:
                max_difference = max(max_difference, nums[i] - premin)
            else:
                premin = nums[i]
        return max_difference
                

