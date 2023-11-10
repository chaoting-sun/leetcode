### binary search

# time complexity: O(len(piles)*lg(max(piles[i])))
# space complexity: O(1)

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def feasible(k):
            return sum(math.ceil(p/k) for p in piles) <= h

        left, right = 1, max(piles)
        while left < right:
            mid = left + (right-left)//2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left