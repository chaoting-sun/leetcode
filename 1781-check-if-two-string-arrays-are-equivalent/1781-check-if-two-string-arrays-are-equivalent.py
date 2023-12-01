# time: O(#characters)
# space: O(1)


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        i, j = 0, 0
        k1, k2 = 0, 0

        while i < len(word1) and j < len(word2):
            while k1 < len(word1[i]) and k2 < len(word2[j]):
                if word1[i][k1] == word2[j][k2]:
                    k1 += 1
                    k2 += 1
                else:
                    return False

            if k1 == len(word1[i]):
                k1 = 0
                i += 1
            if k2 == len(word2[j]):
                k2 = 0
                j += 1

        return i == len(word1) and j == len(word2)


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        i, j = 0, 0
        k1, k2 = 0, 0

        while i < len(word1) and j < len(word2):
            if word1[i][k1] != word2[j][k2]:
                return False
            if k1 == len(word1[i])-1:
                k1 = 0
                i += 1
            else:
                k1 += 1
            if k2 == len(word2[j])-1:
                k2 = 0
                j += 1
            else:
                k2 += 1
        return i == len(word1) and j == len(word2)


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)