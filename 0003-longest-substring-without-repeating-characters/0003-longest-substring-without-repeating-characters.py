class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = {}
        max_len = 0
        sid = 0

        for eid in range(len(s)):
            if s[eid] in chars:
                max_len = max(max_len, eid-sid)
                if chars[s[eid]] >= sid:
                    sid = chars[s[eid]] + 1
                chars[s[eid]] = eid
            else:
                chars[s[eid]] = eid

        return max(max_len, len(s)-sid)

            