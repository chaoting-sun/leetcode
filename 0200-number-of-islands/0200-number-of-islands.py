import numpy as np
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visited = np.zeros((len(grid), len(grid[0])))

        def dfs(grid, i, j, visited):
            visited[i][j] = 1
            if i > 0 and grid[i-1][j] == '1' and not visited[i-1][j]: dfs(grid, i-1, j, visited)
            if i < len(grid)-1 and grid[i+1][j] == '1' and not visited[i+1][j]: dfs(grid, i+1, j, visited)
            if j > 0 and grid[i][j-1] == '1' and not visited[i][j-1]: dfs(grid, i, j-1, visited)
            if j < len(grid[0])-1 and grid[i][j+1] == '1' and not visited[i][j+1]: dfs(grid, i, j+1, visited)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and not visited[i][j]:
                    dfs(grid, i, j, visited)
                    count += 1
        return count