### method: sort

# time complexity: O(nlogn)
# space complexity: O(1)

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        
        coins = 0
        for i in range(len(piles)//3, len(piles), 2):
            coins += piles[i]
        return coins