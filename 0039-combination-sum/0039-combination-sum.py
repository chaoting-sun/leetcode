### backtracking

class Solution(object):
    def backtrack(self, ans, candidates, l, r, prevSet, prevLeft):
        if prevLeft == 0:
            ans.append(prevSet)
            return
        if prevLeft < 0:
            return
        
        for i in range(l, r + 1):
            if candidates[i] <= prevLeft:
                currSet = prevSet + [candidates[i]]
                currLeft = prevLeft - candidates[i]
                print(currSet, currLeft)
                self.backtrack(ans, candidates, i, r, currSet, currLeft)
            else:
                break

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        l, r = 0, len(candidates)-1
        candidates.sort()
        while r > 0 and candidates[r] > target:
            r -= 1

        self.backtrack(ans, candidates, l, r, [], target)
        return ans