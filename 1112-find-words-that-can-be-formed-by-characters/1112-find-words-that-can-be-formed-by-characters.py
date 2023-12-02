class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charCnt = {}
        for ch in chars:
            charCnt[ch] = charCnt.get(ch, 0) + 1

        ans = 0

        for word in words:
            wordCnt = {}
            valid = True
            for ch in word:
                if ch not in charCnt or wordCnt.get(ch,-1) == charCnt.get(ch,-2):
                    valid = False
                    break
                wordCnt[ch] = wordCnt.get(ch, 0) + 1
            if valid:
                ans += len(word)
        
        return ans