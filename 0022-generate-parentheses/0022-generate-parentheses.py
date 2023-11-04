class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(nLeftParentheses, nPairs, track, ans):
            if len(track) == n*2:
                ans.append(track)
                return

            if nPairs == n:
                return
            
            if nLeftParentheses+nPairs < n:
                backtrack(nLeftParentheses+1, nPairs, track+'(', ans) # add (
            if nLeftParentheses > 0:
                backtrack(nLeftParentheses-1, nPairs+1, track+')', ans) # add )

        backtrack(0, 0, '', ans)
        return ans            



