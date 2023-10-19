### bfs; mine (TLE; O(N^2))

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        ans = [[10E6 for _ in range(n)] for _ in range(m)]

        def bfs(i, j):
            visited = [[0 for _ in range(n)] for _ in range(m)]
            q = deque([(i, j)])
            distance = 0

            while q:
                size = len(q)
                
                for i in range(size):
                    pi, pj = q.popleft()
                    if mat[pi][pj] == 0:
                        return distance

                    visited[pi][pj] = 1

                    if pi > 0 and not visited[pi-1][pj]: q.append((pi-1, pj))
                    if pi < m - 1 and not visited[pi+1][pj]: q.append((pi+1, pj))
                    if pj > 0 and not visited[pi][pj-1]: q.append((pi, pj-1))
                    if pj < n - 1 and not visited[pi][pj+1]: q.append((pi, pj+1))
                
                distance += 1

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    ans[i][j] = 0
                else:
                    ans[i][j] = bfs(i, j)
        return ans


### bfs (smarter; multi-source bfs; directly change mat)

# source: https://leetcode.com/problems/01-matrix/solutions/3920110/94-87-multi-source-bfs-queue/?envType=list&envId=rab78cw1
# time complexity: O(mn)
# space complexity: O(mn)

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        q = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = 10E8
        
        level = 0

        while q:
            i1, j1 = q.popleft()

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                i2 = i1 + dx
                j2 = j1 + dy
                if 0 <= i2 < m and 0 <= j2 < n and mat[i2][j2] > mat[i1][j1] + 1:
                    mat[i2][j2] = mat[i1][j1] + 1
                    q.append((i2, j2))
        return mat


### bfs (smartest; multi-source)

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        q = deque()
        seen = set()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                    seen.add((i, j))
        
        level = 1

        while q:
            size = len(q)

            for i in range(size):
                i1, j1 = q.popleft()

                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    i2 = i1 + dx
                    j2 = j1 + dy
                    if 0 <= i2 < m and 0 <= j2 < n and (i2, j2) not in seen:
                        mat[i2][j2] = level
                        seen.add((i2, j2))
                        q.append((i2, j2))
            level += 1
        
        return mat