### method1: mine (TLE)

# class Solution:
#     def bfs(self, llst, i):
#         queue = deque([i])
#         cnt = -1
#         visited = [False] * len(llst)

#         while queue:
#             size = len(queue)
#             cnt += 1
            
#             for i in range(size):
#                 j = queue.popleft()
#                 visited[j] = True

#                 for k in llst[j]:
#                     if not visited[k]:
#                         queue.append(k)
#         return cnt
    
#     def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
#         # build graph
#         llst = [[] for _ in range(n)]

#         for e in edges:
#             llst[e[0]].append(e[1])
#             llst[e[1]].append(e[0])

#         heights = [self.bfs(llst, i) for i in range(n)]
#         minv = min(heights)
#         return [i for i in range(len(heights)) if heights[i] == minv]


### method2: removing leaves

# source: https://leetcode.com/problems/minimum-height-trees/solutions/76055/share-some-thoughts/?envType=list&envId=rab78cw1

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        # build graph
        llst = [set() for _ in range(n)]

        for i, j in edges:
            llst[i].add(j)
            llst[j].add(i)

        leaves = [i for i in range(len(llst)) if len(llst[i]) == 1]

        # remove leaves until n <= 2
        while n > 2:
            newLeaves = []
            n -= len(leaves)
            for i in leaves:
                j = llst[i].pop() # random node connected with i
                llst[j].remove(i)
                if len(llst[j]) == 1:
                    newLeaves.append(j)
            leaves = newLeaves
        return leaves