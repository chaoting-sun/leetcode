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


### method: Floyd's Cycle Detection

# solution: https://www.youtube.com/watch?v=wjYnzkAhcNk
# time complexity: O(N)
# space complexity: O(1)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = slow = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break
        return slow