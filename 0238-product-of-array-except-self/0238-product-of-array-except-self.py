### method1: two arrays: prefix product and suffix product

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixProduct = [1] * n
        suffixProduct = [1] * n

        for i in range(1, n):
            prefixProduct[i] = prefixProduct[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            suffixProduct[i] = suffixProduct[i+1] * nums[i+1]
        
        ans = [1] * n
        for i in range(n):
            ans[i] = prefixProduct[i] * suffixProduct[i]
        return ans


### method2: 