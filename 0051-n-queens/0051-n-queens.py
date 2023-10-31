class Solution:
    def construct(self, board):
        return [''.join(b) for b in board]
    
    def isValid(self, board, rowi, coli):
        # vertical
        for i in range(rowi):
            if board[i][coli] == 'Q':
                return False
        # 45 degree
        i, j = rowi-1, coli-1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        # 135 degree
        i, j = rowi-1, coli+1
        while i >= 0 and j < len(board):
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        return True

    def backtrack(self, board, rowi, m, n, ans):
        if m == n:
            ans.append(self.construct(board))
            return

        for coli in range(n):
            if self.isValid(board, rowi, coli):
                board[rowi][coli] = 'Q'
                self.backtrack(board, rowi+1, m+1, n, ans)
                board[rowi][coli] = '.'

    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []

        board = [['.']*n for _ in range(n)]
        self.backtrack(board, 0, 0, n, ans)
        return ans