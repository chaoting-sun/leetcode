import numpy
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