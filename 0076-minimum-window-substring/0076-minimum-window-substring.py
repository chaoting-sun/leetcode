### sliding window

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        minSubstr = ""
        
        map_t = defaultdict(int)
        for ch in t:
            map_t[ch] += 1
        
        cnt = len(map_t.keys())
        begin, end = 0, 0

        while end < len(s):
            ch = s[end]

            if ch in map_t:
                map_t[ch] -= 1
                if map_t[ch] == 0:
                    cnt -= 1
            
            end += 1

            while cnt == 0:
                tmp_ch = s[begin]
                if tmp_ch in map_t:
                    map_t[tmp_ch] += 1
                    if map_t[tmp_ch] > 0:
                        cnt += 1
                        currLength = end - begin
                        if minSubstr == "" or len(minSubstr) > currLength:
                            minSubstr = s[begin:end]
                begin += 1
        return minSubstr