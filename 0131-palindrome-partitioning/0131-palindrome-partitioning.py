### backtracking

# time complexity: O(N*N^2)
"""
T(N) = T(N-1) + T(N-2) + ... + T(1)
T(N-1) = T(N-2) + T(N-3) + ... + T(1)
-
-----------------------------------
T(N) = 2*T(N-1) = O(2^N)

it takes O(N) to check if a substring is a palindrome,
so the time complexity is O(2^N) * O(N)
"""

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def backtrack(substr, part, ans):
            if not substr:
                ans.append([p for p in part])
                return

            for i in range(math.ceil(len(substr)/2.)):
                # odd palindrome
                delta = 0
                while i-delta >= 0 and substr[i-delta] == substr[i+delta]:
                    delta += 1

                if i - delta == -1:
                    backtrack(substr[i+delta:], part+[substr[:i+delta]], ans)

                # even palindrome

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


### backtracking (cleaner)

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        self.backtrack(s, [], ans)
        return ans

    def backtrack(self, substr, part, ans):
        if not substr:
            ans.append(part)
            return
        for i in range(len(substr)):
            if self.isPalindrome(substr[:i+1]):
                self.backtrack(substr[i+1:], part+[substr[:i+1]], ans)

    def isPalindrome(self, substr):
        return substr == substr[::-1]