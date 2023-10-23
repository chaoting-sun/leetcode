### method1: bfs (multi-source bfs)

# time complexity: O(mn)
# space complexity: O(mn)

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        q = deque()

        for i in range(m):
            if board[i][0] == 'O': q.append((i, 0))
            if board[i][n-1] == 'O': q.append((i, n-1))
        for j in range(n):
            if board[0][j] == 'O': q.append((0, j))
            if board[m-1][j] == 'O': q.append((m-1, j))

        while q:
            size = len(q)

            for i in range(size):
                x, y = q.popleft()
                if board[x][y] != 'O':
                    continue
                board[x][y] = '#'
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    newx = x + dx
                    newy = y + dy
                    if 0 <= newx < m and 0 <= newy < n and board[newx][newy] == 'O':
                        q.append((newx, newy))

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'


### method2: bfs

# time complexity: O(mn)
# space complexity: O(mn)

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        def dfs(i, j, m, n):
            if not 0 <= i < m or not 0 <= j < n or board[i][j] != 'O':
                return
            board[i][j] = '#'
            dfs(i+1, j, m, n)
            dfs(i-1, j, m, n)
            dfs(i, j+1, m, n)
            dfs(i, j-1, m, n)

        for i in range(m):
            if board[i][0] == 'O': dfs(i, 0, m, n)
            if board[i][n-1] == 'O': dfs(i, n-1, m, n)
        for j in range(n):
            if board[0][j] == 'O': dfs(0, j, m, n)
            if board[m-1][j] == 'O': dfs(m-1, j, m, n)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O': board[i][j] = 'X'
                if board[i][j] == '#': board[i][j] = 'O'