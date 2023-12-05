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


### method4: dp with tabulation
# optimal substructure: the LIS ending at index i
# time complexity: O(n^2)
# space complexity: O(n)

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


### method5: binary search

# time complexity: O(nlogn)
# space complexity: O(n)

import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subseq = []
        for k in nums:
            if not subseq or subseq[-1] < k:
                subseq.append(k)
            else:
                ip = bisect.bisect_left(subseq, k)
                subseq[ip] = k        
        return len(subseq)


### method6: binary search + inplace space

# time complexity: O(nlogn)
# space complexity: O(1)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        pos = 0
        for k in nums:
            if pos == 0 or nums[pos-1] < k:
                nums[pos] = k
                pos += 1
            else:
                ip = bisect.bisect_left(nums, k, lo=0, hi=pos-1)
                nums[ip] = k
        return pos