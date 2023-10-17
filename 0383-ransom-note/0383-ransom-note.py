class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = defaultdict(int)
        for ch in magazine:
            m[ch] += 1
        for ch in ransomNote:
            if ch not in m:
                return False
            m[ch] -= 1
            if m[ch] < 0:
                return False
        return True