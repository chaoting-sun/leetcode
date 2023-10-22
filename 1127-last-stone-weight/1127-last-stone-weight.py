### method1: heap
# time complexity: O(NlogN)
# space complexity: O(N)

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = []

        for v in stones:
            heapq.heappush(maxheap, -v)

        while len(maxheap) > 1:
            maxv1 = -heapq.heappop(maxheap)
            maxv2 = -heapq.heappop(maxheap)

            if maxv1 > maxv2:
                newv = maxv1 - maxv2
                heapq.heappush(maxheap, -newv)
        
        if not maxheap:
            return 0
        return -maxheap[0]