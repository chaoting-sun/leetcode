### method1: two pointers

# time complexity: O(N)
# space complexity: O(1)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        left, right = 0, n - 1

        while left <= right:
            # move to the next character that is alphameric
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            # if the left and right crossovered, stop
            # if left > right: break

            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        
        return True