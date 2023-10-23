class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def backtrack(substr, part, ans):
            if not substr:
                ans.append([p for p in part])
                return

            for i in range(math.ceil(len(substr)/2.)):
                delta = 0
                while i-delta >= 0 and substr[i-delta] == substr[i+delta]:
                    delta += 1

                if i - delta == -1:
                    backtrack(substr[i+delta:], part+[substr[:i+delta]], ans)

                if i + 1 >= len(substr):
                    break

                left, right = i, i+1
                while left >= 0 and right < len(substr) and substr[left] == substr[right]:
                    left -= 1
                    right += 1
                if left == -1:
                    backtrack(substr[right:], part+[substr[:right]], ans)

        backtrack(s, [], ans)
        return ans