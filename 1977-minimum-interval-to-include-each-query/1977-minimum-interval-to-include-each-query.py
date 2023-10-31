class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        n = len(intervals)
        ans = [-1] * len(queries)
        
        intervals.sort()
        queries_id = sorted((q, qi) for qi, q in enumerate(queries))

        j = 0
        minheap = []

        for q, qi in queries_id:
            while j < n and intervals[j][0] <= q:
                left, right = intervals[j]
                heapq.heappush(minheap, (right-left+1, right))
                j += 1
            
            while minheap and minheap[0][1] < q:
                heapq.heappop(minheap)
            
            if minheap:
                ans[qi] = minheap[0][0]
            
        return ans

