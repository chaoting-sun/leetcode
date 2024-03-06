class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1list, word2list = [*word1], [*word2]

        i = 0
        ans = []

        len1, len2 = len(word1), len(word2)
        minLen = min(len1, len2)

        while i < minLen:
            ans.append(word1list[i])
            ans.append(word2list[i])
            i += 1
                
        if len1 > len2:
            ans.extend(word1list[i:])
        elif len1 < len2:
            ans.extend(word2list[i:])

        return "".join(ans)