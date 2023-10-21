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


### method3: quick select (modified version from quick sort; TLE)

# source: https://leetcode.com/problems/k-closest-points-to-origin/solutions/220235/java-three-solutions-to-this-classical-k-th-problem/comments/430257
# time complexity: best O(N); worst O(N^2) (N+N/2+N/4+...)
# space complexity: O(1) (we directly modify the array)

# class Solution:
#     def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
#         def quickSelect(A, l, r):
#             pivot = A[r] # use the right-most element as pivot
#             i = l
#             for j in range(l, r):
#                 # switch element to left-most if smaller than pivot
#                 if A[j][0]**2 + A[j][1]**2 <= pivot[0]**2 + pivot[1]**2:
#                     A[i], A[j] = A[j], A[i]
#                     i += 1
#             # put pivot into correct place
#             A[i], A[r] = A[r], A[i]
            
#             return i
        

#         n = len(points)
#         l, r = 0, n-1
        
#         while l <= r:
#             mid = quickSelect(points, l, r)

#             if mid == K-1: return points[:K]
#             elif mid < K-1: 
#                 l = mid + 1
#             else:
#                 r = mid - 1