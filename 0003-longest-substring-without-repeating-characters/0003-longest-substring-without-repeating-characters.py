### method1: hashmap

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        max_len = 0
        left = 0

        for right in range(len(s)):
            if s[right] in chars:
                max_len = max(max_len, right-left)
                if chars[s[right]] >= left:
                    left = chars[s[right]] + 1
            chars[s[right]] = right

        return max(max_len, len(s)-left)


### method2: set

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        chars = set()
        max_len = 0

        for right in range(len(s)):
            if s[right] not in chars:
                chars.add(s[right])
                max_len = max(max_len, right - left + 1)
            else:
                while s[right] in chars:
                    chars.remove(s[left])
                    left += 1
                chars.add(s[right])
        return max_len


### method3: integer array

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        max_len = 0
        chars = [-1] * 128

        for right in range(len(s)):
            if chars[ord(s[right])] >= left:
                left = chars[ord(s[right])] + 1
            chars[ord(s[right])] = right
            max_len = max(max_len, right - left + 1)
        return max_len