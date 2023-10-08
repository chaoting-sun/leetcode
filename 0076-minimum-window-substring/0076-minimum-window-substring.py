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

        while right < size:

            if s[right] in record and record[s[right]] > 0:
                cnt -= 1
            
            if s[right] not in record:
                record[s[right]] = 0
            record[s[right]] -= 1

            right += 1

            while cnt == 0:
                if right - left < minLen:
                    minLeft = left
                    minLen = right - left
                record[s[left]] += 1
                if record[s[left]] > 0:
                    cnt += 1
                left += 1                
        
        if minLen == 10E5:
            return ''
        return s[minLeft: minLeft+minLen]