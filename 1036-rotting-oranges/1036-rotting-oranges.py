### bfs

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque([])

        orange_cnt = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] != 0:
                    orange_cnt += 1

        if orange_cnt == 0 and len(q) == 0:
            return 0

        rotten_cnt = 0
        time = -1

        while q:
            size = len(q)
            time += 1
            for i in range(size):
                x, y = q.popleft()
                rotten_cnt += 1

                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    newx = x + dx
                    newy = y + dy
                    if not 0 <= newx < m or not 0 <= newy < n:
                        continue
                    if grid[newx][newy] == 1:
                        q.append((newx, newy))
                        grid[newx][newy] = 2
        
        if rotten_cnt == orange_cnt:
            return time
        return -1       
