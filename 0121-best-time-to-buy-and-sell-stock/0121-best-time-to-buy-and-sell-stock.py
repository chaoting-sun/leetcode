class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        minV, maxProfit = prices[0], 0

        for i in range(1, len(prices)):
            maxProfit = max(maxProfit, prices[i]-minV)
            minV = min(minV, prices[i])
        return maxProfit

        
        