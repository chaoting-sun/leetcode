class Solution:
    def dfs(self, board, i, j, word):
        if len(word) == 0: # all characters are checked
            return True
        
        if not 0 <= i < len(board) or not 0 <= j < len(board[0]):
            return False

        if board[i][j] != word[0]:
            return False

        tmp = board[i][j]
        board[i][j] = '#'

        res = self.dfs(board, i-1, j, word[1:]) or \
            self.dfs(board, i+1, j, word[1:]) or \
            self.dfs(board, i, j-1, word[1:]) or \
            self.dfs(board, i, j+1, word[1:])

        board[i][j] = tmp
        return res

    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False
        