### method: backtracking

nDiff2Permut = { 1: 1, 2: 3, 3: 6 }

class Solution:
    def backtrack(self, iChild, nLeft, limit, nDistinct, prev, cnt):
        if iChild == 2:
            if prev != nLeft:
                nDistinct += 1
            return cnt + nDiff2Permut[nDistinct]
         
        upperBound = min(nLeft, limit, prev)
        lowerBound = math.ceil(nLeft / (3-iChild))
        
        for nCandy in range(lowerBound, upperBound+1):
            nD = nDistinct if prev == nCandy else nDistinct + 1
            cnt = self.backtrack(iChild+1, nLeft-nCandy, limit, nD, nCandy, cnt)
        
        return cnt        
    
    
    def distributeCandies(self, n: int, limit: int) -> int:
        if n / 3 > limit:
            return 0
        return self.backtrack(0, n, limit, 0, 10E7, 0)