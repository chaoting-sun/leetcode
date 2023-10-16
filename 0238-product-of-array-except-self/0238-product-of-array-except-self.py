class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        prefixProduct = [1] * size
        suffixProduct = [1] * size

        prefixProduct[0] = nums[0]
        suffixProduct[size-1] = nums[size-1]

        for i in range(1, size):
            prefixProduct[i] = prefixProduct[i-1] * nums[i]
        for i in range(size-2, -1, -1):
            suffixProduct[i] = suffixProduct[i+1] * nums[i]
        
        ans = [1] * size
        ans[0], ans[size-1] = suffixProduct[1], prefixProduct[size-2]
        for i in range(1, size-1):
            ans[i] = prefixProduct[i-1] * suffixProduct[i+1]
        return ans
        
        
        