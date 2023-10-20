# method: binary search

# time complexity = O(logN)
# space complexity: O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            c = l + (r-l)//2
            if nums[c] > target:
                r = c - 1
            elif nums[c] < target:
                l = c + 1
            else:
                return c
            
        return -1