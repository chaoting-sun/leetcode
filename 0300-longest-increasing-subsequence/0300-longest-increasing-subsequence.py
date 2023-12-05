### method1: bruteforce (TLE)

# time complexity: O(2^n)
# space complexity: O(n)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def solve(nums, i, prev):
            if i >= len(nums):
                return 0
            # take and dontTake the current value
            take = 0
            if prev == -1 or nums[i] > nums[prev]:
                take = 1 + solve(nums, i+1, i)
            dontTake = solve(nums, i+1, prev)
            return max(take, dontTake)
        
        return solve(nums, 0, -1)


### method2: dp with memoization
# optimal substructure: the max length of the increasing subsequence
# starting at ith element with previously picked element prev

# time complexity: O(n^2)
# space complexity: O(n^2)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def solve(nums, i, prev, dp):
            if i >= len(nums):
                return 0
            if dp[i][prev+1] != -1:
                return dp[i][prev+1]
            # take and dontTake the current value
            take = 0
            if prev == -1 or nums[i] > nums[prev]:
                take = 1 + solve(nums, i+1, i, dp)
            dontTake = solve(nums, i+1, prev, dp)
            dp[i][prev+1] = max(take, dontTake)
            return dp[i][prev+1]

        n = len(nums)
        dp = [[-1]*(n+1) for _ in range(n)] # dp[i][j] := max LIS starting from i when nums[j] is previously picked element
        return solve(nums, 0, -1, dp)


### method3: dp with memoization with optimized space
# optimal substructure: the LIS starting at index i
# time complexity: O(n^2)
# space complexity: O(n)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def solve(nums, i, prev, dp):
            if i >= len(nums):
                return 0
            if dp[prev+1] != -1:
                return dp[prev+1]
            # take and dontTake the current value
            take = 0
            if prev == -1 or nums[i] > nums[prev]:
                take = 1 + solve(nums, i+1, i, dp)
            dontTake = solve(nums, i+1, prev, dp)
            dp[prev+1] = max(take, dontTake)
            return dp[prev+1]

        dp = [-1] * (len(nums)+1)
        return solve(nums, 0, -1, dp)


### method1: dp with tabulation
# optimal substructure: the LIS ending at index i
# time complexity: O()
# space complexity: O()

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        ans = 1

        for i in range(n):
            for prev in range(i):
                if nums[prev] < nums[i]:
                    dp[i] = max(dp[i], dp[prev]+1)
                    ans = max(ans, dp[i])
        return ans        


# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         n = len(nums)
#         dp = [1] * n

#         for r in range(n):
#             for l in range(r):
#                 if nums[l] < nums[r] and dp[r]



#         return maxLength

