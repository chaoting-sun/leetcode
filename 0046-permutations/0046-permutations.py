class Solution(object):
    def dfs(self, prevNums, maxL, prevSet, ans):
        if len(prevSet) == maxL:
            ans.append(prevSet)
            return
        
        for i in range(len(prevNums)):
            curSet = prevSet + [prevNums[i]]
            curNums = prevNums[:i] + prevNums[i+1:]
            self.dfs(curNums, maxL, curSet, ans)

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        self.dfs(nums, len(nums), [], ans)
        return ans