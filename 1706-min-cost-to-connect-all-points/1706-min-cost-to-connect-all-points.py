### method1: Kruskal's Algorithm

# time complexity: O(V^2 lgV)
# space complexity: O(V^2)

class UnionFind:
    def __init__(self, n):
        self.rank = [1] * n
        self.parent = [i for i in range(n)]
    
     # pass compression
    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]            

    # union by rank
    def union(self, x, y):
        p1, p2 = self.find(x), self.find(y)
        if p1 == p2:
            return
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p2] = p1
            self.rank[p1] += 1

class Solution:
    def weight(self, p1, p2):
        return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        uf = UnionFind(n)

        minheap = []
        
        for i in range(n-1):
            for j in range(i+1, n):
                w = self.weight(points[i], points[j])
                heapq.heappush(minheap, (w, i, j))

        totalWeights = 0
        cnt = 0

        while cnt < n-1:
            w, i, j = heapq.heappop(minheap)
            if uf.find(i) != uf.find(j):
                totalWeights += w
                uf.union(i, j)
                cnt += 1

        return totalWeights


### method2: Prim's Algorithm

# time complexity: O(V^2 lgV)
# space complexity: O(V^2)

class Solution:
    def weight(self, p1, p2):
        return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        minheap = [(0, 0)] # (w, u)
        mstPoints = set()
        totalWeights = 0

        while minheap:
            w, u = heapq.heappop(minheap)
            if u in mstPoints:
                continue
            
            mstPoints.add(u)
            totalWeights += w

            for v in range(n):
                if v not in mstPoints:
                    w = self.weight(points[u], points[v])
                    heapq.heappush(minheap, (w, v))

            if len(mstPoints) == n:
                break
        return totalWeights


### method2.1: Prim's Algorithm (optimized) (cannot understand)
# source: https://leetcode.com/problems/min-cost-to-connect-all-points/solutions/843940/c-mst-kruskal-prim-s-complete-graph/