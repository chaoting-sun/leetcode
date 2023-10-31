### priority queue (min heap)

# source: https://www.youtube.com/watch?v=5hQ5WWW5awQ
# method: Sort both the queries and intervals so that we can handle queries from small to large values. Use a min heap to store the valid intervals for current query, which easily yield the smallest interval. The intervals in the min heap valid for the current query are left for the following queries as they may be valid for them. However, those invalid for the current query should be popped as they must not be valid for the following queries.

# time complexity: O(NlogN+QlogQ) (N = len(intervals); Q = len(queries))
# space complexity: O(N)

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


### union find (hard to understand)
# method: https://leetcode.com/problems/minimum-interval-to-include-each-query/solutions/1186840/python-union-find/?envType=list&envId=rr2ss0g5