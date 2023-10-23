class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        mp = {}

        for n in nums:
            if n not in mp:
                left = right = 0
                if n-1 in mp: left = mp[n-1]
                if n+1 in mp: right = mp[n+1]

                mp[n] = left + 1 + right
                
                mp[n-left] = mp[n]
                mp[n+right] = mp[n]

                if mp[n] > res:
                    res = mp[n]
        return res