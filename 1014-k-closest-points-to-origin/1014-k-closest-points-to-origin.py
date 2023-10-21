### method1: sort
# time complexity: O(NlogN)
# space complexity: O(N)

from numpy import argsort
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis = [x**2+y**2 for x, y in points]
        smallIndices = argsort(dis)[:k]
        return [points[i] for i in smallIndices]


### method2: heap
# time complexity:
# space complexity

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis = [x**2+y**2 for x, y in points]
        maxheap = []
        for i, d in enumerate(dis):
            heapq.heappush(maxheap, (-d, i))
            if len(maxheap) > k:
                heapq.heappop(maxheap)
        ans = []
        while maxheap:
            i = heapq.heappop(maxheap)[1]
            ans.append(points[i])
        return ans