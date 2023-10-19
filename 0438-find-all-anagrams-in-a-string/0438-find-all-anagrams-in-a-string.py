### method: sliding window
# source: https://www.youtube.com/watch?v=G8xtZy0fDKg

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        
        sCount, pCount = {}, {}
        for i in range(len(p)):
            pCount[p[i]] = 1 + pCount.get(p[i], 0)
            sCount[s[i]] = 1 + sCount.get(s[i], 0)

        res = [0] if pCount == sCount else []

        l = 0
        for i in range(len(p), len(s)):
            sCount[s[i]] = 1 + sCount.get(s[i], 0)
            sCount[s[l]] -= 1

            if sCount[s[l]] == 0:
                sCount.pop(s[l])

            l += 1
            
            if sCount == pCount:
                res.append(l)
        return res


### method2: sliding window

# source: https://leetcode.com/problems/find-all-anagrams-in-a-string/solutions/92007/sliding-window-algorithm-template-to-solve-all-the-leetcode-substring-search-problem/?envType=list&envId=rab78cw1

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        mp = {}
        for c in p:
            mp[c] = 1 + mp.get(c, 0)
        
        res = []
        count = len(mp)
        begin, end = 0, 0

        while end < len(s):
            c = s[end]

            if c in mp:
                mp[c] = mp.get(c, 0) - 1
                if mp[c] == 0:
                    count -= 1
            
            end += 1

            while count == 0:
                tempc = s[begin]
                if tempc in mp:
                    mp[tempc] += 1
                    if mp[tempc] > 0:
                        count += 1
                
                if end - begin == len(p):
                    res.append(begin)
                begin += 1
        return res