### method1: dp (O(n^2); MLE)

# [ Explanation ]
# optimal substructure: dp[i][j] := the max sum of the subarray nums[m:j], where 0 <= m <= j
# if i == j: dp[i][j] = nums[i]
# if i != j: dp[i][j] = nums[i] + (dp[i][j-1] > 0 ? dp[i][j-1] : 0)
# We only need to take care about dp[i][j] where i <= j

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [[0]*len(nums) for _ in range(len(nums))]

        maxSum = float("-inf")

        for j in range(len(nums)):
            for i in range(j+1):
                dp[i][j] = nums[j]
                if j > 0 and dp[i][j-1] > 0:
                    dp[i][j] += dp[i][j-1]
                maxSum = max(maxSum, dp[i][j])

        return maxSum

### method2: Kadane's algorithm (O(n))

# [ Explanation ]
# traverse from left to right
# currMaxSum := the max sum of the subarray, which includes the current value
# maxSum := the max subarray until now

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