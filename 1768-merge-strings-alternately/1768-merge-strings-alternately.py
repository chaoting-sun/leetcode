### straightforward
# time complexity: O(n+m)
# space complexity: O(n+m)

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        ans = []

        len1, len2 = len(word1), len(word2)
        minLen = min(len1, len2)

        while i < minLen:
            ans.append(word1[i])
            ans.append(word2[i])
            i += 1
                
        if len1 > len2:
            ans.extend(word1[i:])
        elif len1 < len2:
            ans.extend(word2[i:])

        return "".join(ans)


# cleaner

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        ans = []

        while i < len(word1) or j < len(word2):
            if i < len(word1):
                ans.append(word1[i])
                i += 1
            if j < len(word2):
                ans.append(word2[j])
                j += 1
        
        return "".join(ans)