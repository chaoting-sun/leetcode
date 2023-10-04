class Solution(object):
    def search(self, candidates, prevl, r, prevSum, prevComb, ans):
        if prevSum == 0:
            ans.append(prevComb)
            return

        elif prevSum < 0:
            return
        
        currl = prevl
        while currl <= r and candidates[currl] <= prevSum:
            currSum = prevSum - candidates[currl]
            currComb = prevComb + [candidates[currl]]
            self.search(candidates, currl, r, currSum, currComb, ans)
            currl += 1

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        comb = []
        l, r = 0, len(candidates) - 1
        candidates.sort()

        while r >= 0 and candidates[r] > target:
            r -= 1
        self.search(candidates, l, r, target, comb, ans)
        return ans