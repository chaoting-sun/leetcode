# method1

class Solution(object):
    def binarySearch(self, nums, l, r, target):
        while l <= r:
            c = (l + r) // 2
            if nums[c] == target:
                return c
            elif nums[c] > target:
                r = c - 1
            elif nums[c] < target:
                l = c + 1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        l, r = 0, n - 1

        while l < r:
            c = (l + r) // 2
            if nums[c] < nums[r]:
                r = c
            else:
                l = c + 1
        pivot = l

        if pivot == 0:
            return self.binarySearch(nums, 0, n-1, target)
        else:
            if nums[0] <= target <= nums[pivot-1]:
                return self.binarySearch(nums, 0, pivot-1, target)
            else:
                return self.binarySearch(nums, pivot, n-1, target)


# method2 (hard to understand)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        l, r = 0, n - 1

        while l <= r:
            c = (l + r) // 2

            if nums[c] == target:
                return c
            
            if nums[l] <= nums[c]:
                if nums[l] <= target < nums[c]:
                    r = c - 1
                else:
                    l = c + 1
            else:
                if nums[c] < target <= nums[r]:
                    l = c + 1
                else:
                    r = c - 1
        return -1