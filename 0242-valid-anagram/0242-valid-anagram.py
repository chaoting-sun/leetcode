class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = {}
        for ch in s:
            if ch in sdict:
                sdict[ch] += 1
            else:
                sdict[ch] = 1
        for ch in t:
            if ch not in sdict:
                return False
            else:
                sdict[ch] -=1
        for v in sdict.values():
            if v != 0:
                return False
        return True