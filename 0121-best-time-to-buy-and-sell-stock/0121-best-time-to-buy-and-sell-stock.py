class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        minV, maxProfit = prices[0], 0

        for i in range(1, len(prices)):
            maxProfit = max(maxProfit, prices[i]-minV)
            minV = min(minV, prices[i])
        return maxProfit

# nice source: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solutions/39038/kadane-s-algorithm-since-no-one-has-mentioned-about-this-so-far-in-case-if-interviewer-twists-the-input/?envType=list&envId=rab78cw1