### method: binary search

# source: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/solutions/158940/beat-100-very-simple-python-very-detailed-explanation/?envType=list&envId=rr2ss0g5
# time complexity: O(logN)
# space complexity: O(1)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        # we try to find the minimum value
        while l < r:
            c = l + (r-l)//2
            if nums[c] > nums[r]:
                l = c + 1
            else:
                # nums[c] <= nums[r]
                r = c
        return nums[l]


### another binary search

# source: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/solutions/48493/compact-and-clean-c-solution/?envType=list&envId=rr2ss0g5

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        while l < r:
            if nums[l] < nums[r]: # ex: 1 2 3 4 5
                break

            c = l + (r-l)//2
            if nums[l] <= nums[c]: # '='? -> ex: 2 1
                l = c + 1
            else:
                r = c
        return nums[l]