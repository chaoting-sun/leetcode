### method1: Pure DFS

# time complexity: O(sum of string length)
# space complexity: O(len(board)*len(board[0]))

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        positions = defaultdict(list)

        for i in range(m):
            for j in range(n):
                positions[board[i][j]].append((i,j))

        def dfs(i, j, board, word, wi):
            if wi == len(word)-1:
                return True

            tmp = board[i][j]
            board[i][j] = '#'
            
            res = False
            for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                newi, newj = i+di, j+dj
                if not 0 <= newi < m or not 0 <= newj < n or board[newi][newj] == '#':
                    continue
                if word[wi+1] == board[newi][newj]:
                    res = dfs(newi, newj, board, word, wi+1)
                if res:
                    break
            board[i][j] = tmp
            return res

        ans = []
        
        for word in words:
            if word[0] not in positions:
                continue
            
            for i, j in positions[word[0]]:
                if dfs(i, j, board, word, 0):
                    ans.append(word)
                    break

        return ans


### DFS + Trie

class TrieNode:
    def __init__(self, isWord=False):
        self.chars = {}
        self.isWord = isWord

class Solution:
    def buildTrie(self, words):
        trie = TrieNode()
    
        for word in words:
            t = trie
            for w in word:
                if w not in t.chars:
                    t.chars[w] = TrieNode()
                t = t.chars[w] # go to the next layer
            t.isWord = True
        return trie
    
    def dfs(self, board, i, j, t, track, ans):
        if t.isWord:
            ans.append(track)
            t.isWord = False # prevent repeated addition

        if not t.chars: # finished traversal
            return
        
        tmp = board[i][j]
        board[i][j] = '#'

        for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
            newi, newj = i+di, j+dj
            if not 0 <= newi < len(board) or not 0 <= newj < len(board[0]) or board[newi][newj] == '#':
                continue
            newCh = board[newi][newj]
            if newCh in t.chars:
                self.dfs(board, newi, newj, t.chars[newCh], track+newCh, ans)
        
        board[i][j] = tmp


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = self.buildTrie(words)
        
        ans = []
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                ch = board[i][j]
                if ch in trie.chars:
                    t = trie
                    self.dfs(board, i, j, t.chars[ch], ch, ans)
        return ans