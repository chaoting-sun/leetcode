class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [10E5] * (1 + amount)
        dp[0] = 0

        coins.sort()

        for i in range(1, amount+1):
            for c in coins:
                if i < c:
                    break
                if dp[i-c] != 10E5:
                    dp[i] = min(dp[i], dp[i-c]+1)
        return dp[amount] if dp[amount] != 10E5 else -1
        