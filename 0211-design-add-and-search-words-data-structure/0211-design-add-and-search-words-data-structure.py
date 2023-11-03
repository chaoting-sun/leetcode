class TrieNode:
    def __init__(self, isWord=False):
        self.chars = {}
        self.isWord = isWord


class WordDictionary:

    def __init__(self):
        self.trie = TrieNode()

    def addWord(self, word: str) -> None:
        t = self.trie
        for w in word:
            if w not in t.chars:
                t.chars[w] = TrieNode()
            t = t.chars[w]
        t.isWord = True

    def search(self, word: str) -> bool:
        
        def helper(i, t):
            if i == len(word):
                if t.isWord:
                    return True
                else:
                    return False

            if word[i] == '.':
                for c in t.chars:
                    if helper(i+1, t.chars[c]):
                        return True
            else:
                if word[i] in t.chars and helper(i+1, t.chars[word[i]]):
                    return True
            return False
        
        return helper(0, self.trie)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)