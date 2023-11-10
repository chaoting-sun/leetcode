class Solution:

    def backtrack(self, nums, start, track, ans):
        if start == len(nums):
            ans.append(track)
            return

        end = start + 1
        while end < len(nums) and nums[start] == nums[end]:
            end += 1

        for i in range(end-start+1):
            newtrack = track + [nums[start]] * i
            self.backtrack(nums, end, newtrack, ans)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        self.backtrack(nums, 0, [], ans)
        return ans