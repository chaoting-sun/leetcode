### method1: bfs

# time complexity: O(N*26^m). N = len(wordList), m = len(beginWord)
# space complexity: O(N)

# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         if endWord not in wordList: return 0

#         wordSet = set(wordList)
#         wordLen = len(beginWord)
        
#         queue = [beginWord]
#         step = 1

#         while len(queue):
#             size = len(queue)
            
#             for i in range(size):
#                 currWord = queue.pop(0)
#                 if currWord == endWord:
#                     return step

#                 for l in range(wordLen):
#                     for c in 'abcdefghijklmnopqrstuvwxyz':
#                         tmpWord = currWord[:l] + c + currWord[l+1:]
#                         if tmpWord in wordSet:
#                             queue.append(tmpWord)
#                             wordSet.remove(tmpWord)
#             step += 1
#         return 0                    


### method: bfs

# time complexity: O(N*m^2)
# space complexity: O(Nm)

# source: https://www.youtube.com/watch?v=h9iTnkgv05E
                
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0

        nei = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j+1:]
                nei[pattern].append(word)
        
        visited = set([beginWord])
        queue = deque([beginWord])
        step = 1
        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return step
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j+1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visited:
                            queue.append(neiWord)
                            visited.add(neiWord)
            step += 1
        return 0