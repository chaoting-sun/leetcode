### method1: hash table

# source: https://leetcode.com/problems/longest-consecutive-sequence/?envType=list&envId=rr2ss0g5
# time complexity: O(N)
# space complexity: O(N)

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


### method2: hash table

# source: https://www.cnblogs.com/grandyang/p/4276225.html
# time complexity: O(N)
# space complexity: O(N)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        st = set(nums) # set

        for n in nums:
            if n not in st:
                continue
            
            st.remove(n)

            left = right = 1
            while n - left in st:
                st.remove(n-left)
                left += 1
            while n + right in st:
                st.remove(n+right)
                right += 1
            
            res = max(res, right+left-1)
        return res