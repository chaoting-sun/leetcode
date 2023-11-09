class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            colset = set()
            for j in range(9):
                if board[i][j] in colset:
                    return False
                if board[i][j] != '.':
                    colset.add(board[i][j])
        
        for i in range(9):
            rowset = set()
            for j in range(9):
                if board[j][i] in rowset:
                    return False
                if board[j][i] != '.':
                    rowset.add(board[j][i])

        for i in (0, 3, 6):
            for j in (0, 3, 6):
                cellset = set()
                for c1 in range(3):
                    for c2 in range(3):
                        print(i+c1, j+c2)
                        if board[i+c1][j+c2] in cellset:
                            return False
                        if board[i+c1][j+c2] != '.':
                            cellset.add(board[i+c1][j+c2])
        return True