### method1: dfs (TLE)

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        cache = {}
        
        def helper(sid, target):
            if (sid, target) in cache:
                return cache[(sid, target)]
            
            if target < 0:
                return False
            if target == 0:
                return True

            # sid: start id of nums
            # target: target sum (left)
            
            for i in range(sid, len(nums)):
                if helper(i+1, target-nums[i]):
                    return True
            cache[(sid, target)] = False
            return False
        
        return False if s%2 else helper(0, s/2)


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        _sum = sum(nums)
        _num = len(nums)

        if _sum % 2:
            return False

        dp = [[True for _ in range(1+_sum)] for _ in range(1+_num)]
        dp[0][0] = True
        for i in range(1, _num+1):
            dp[i][0] = True
        for j in range(1, _sum+1):
            dp[0][j] = False
        
        for i in range(1, _num+1):
            for j in range(1, _sum+1):
                dp[i][j] = dp[i-1][j]
                if j >= nums[i-1]:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
        return dp[_num][_sum//2]        