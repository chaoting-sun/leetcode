### method1: hash table

# time complexity: O(N_ransomNote+N_magazine) 
# space complexity: O(26)

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


### method2: array

# time complexity: O(N_ransomNote+N_magazine) 
# space complexity: O(26)

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        alphabet = [0] * 26
        
        for ch in magazine:
            alphabet[ord(ch)-ord('a')] += 1
        for ch in ransomNote:
            alphabet[ord(ch)-ord('a')] -= 1
            if alphabet[ord(ch)-ord('a')] < 0:
                return False
        return True