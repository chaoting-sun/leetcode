# sliding window (hard)

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        record = {}
        for c in t:
            if c in record: record[c] += 1
            else: record[c] = 1
        
        size = len(s)
        cnt = len(t)
        left, right = 0, 0
        minLeft, minLen = 0, 10E5

        # 'right' starts from 0 and moves to find a valid window
        while right < size:
            # decrease cnt if s[right] in record
            if s[right] in record and record[s[right]] > 0:
                cnt -= 1
            
            # decrease record[s[right]], including s[right] not in t
            if s[right] not in record:
                record[s[right]] = 0
            record[s[right]] -= 1

            right += 1

            # when we find a valid window, move right to find a smaller window s.t. cnt is still 0
            while cnt == 0:
                if right - left < minLen:
                    minLeft = left
                    minLen = right - left
                record[s[left]] += 1
                # when s[left] in t and s[left] > 0 then increase cnt
                if record[s[left]] > 0:
                    cnt += 1
                left += 1                
        
        if minLen == 10E5:
            return ''
        return s[minLeft: minLeft+minLen]

    
# nice source: https://leetcode.com/problems/minimum-window-substring/solutions/26808/here-is-a-10-line-template-that-can-solve-most-substring-problems/?envType=list&envId=rab78cw1