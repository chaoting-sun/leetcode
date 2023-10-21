### method1: dp (O(n^2); TLE)

import numpy as np

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = np.zeros((n,n), dtype=int)
        maxSum = -10E4

        for j in range(n):
            for i in range(j+1):
                if i == j:
                    dp[i][j] = nums[i]
                else:
                    dp[i][j] = dp[i][j-1] + nums[j]
                maxSum = max(maxSum, dp[i][j])
        return maxSum


### method2: Kadane's algorithm (O(n))

import numpy as np

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        maxSum = currMaxSum = nums[0]
        
        for i in range(1, n):
            if currMaxSum > 0:
                currMaxSum += nums[i]
            else:
                currMaxSum = nums[i]
            maxSum = max(maxSum, currMaxSum)
        return maxSum


### method3: prefix sum (O(n))

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        prefixSum = [0] * (n+1)
        prefixSum[0] = 0
        for i in range(n):
            prefixSum[i+1] = prefixSum[i] + nums[i]
        minSum = float('inf')
        maxSum = -float('-inf')

        for i in range(1, n+1):
            minSum = min(minSum, prefixSum[i-1])
            maxSum = max(maxSum, prefixSum[i] - minSum)
        return maxSum


### method3.1 prefix sum (faster)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        minSum = 0
        maxSum = float('-inf')
        prefixSum = 0

        for k in nums:
            prefixSum += k
            maxSum = max(maxSum, prefixSum-minSum)
            minSum = min(minSum, prefixSum)
        return maxSum