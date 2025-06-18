class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n = len(nums)
        sorted_nums = sorted(nums)
        ans = []

        for i in range(0, n, 3):
            if sorted_nums[i+2] - sorted_nums[i] > k:
                return []
            else:
                ans.append(sorted_nums[i:i+3])

        return ans