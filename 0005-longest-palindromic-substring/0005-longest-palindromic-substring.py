class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        stk1 = []
        stk2 = []
        curr = right = 0
        max_len = 1
        ans = s[0]

        while curr < len(s):
            if len(stk1) >= 1 and stk1[-1] == s[curr]:
                right = curr
                while len(stk1) and right < len(s) and stk1[-1] == s[right]:
                    stk2.append(stk1.pop(-1))
                    right += 1

                curr_len = 2 * (right - curr)
                # print('1:', curr_len, right, curr)
                if curr_len > max_len:
                    max_len = curr_len
                    ans = s[len(stk1):right]

                while len(stk2):
                    stk1.append(stk2.pop(-1))
            
            # print('1:', ans, max_len, stk1, stk2)

            if len(stk1) >= 2 and stk1[-2] == s[curr]:
                right = curr
                stk2.append(stk1.pop(-1))
                while len(stk1) and right < len(s) and stk1[-1] == s[right]:
                    stk2.append(stk1.pop(-1))
                    right += 1

                curr_len = 2 * (right - curr) + 1
                if curr_len > max_len:
                    max_len = curr_len
                    ans = s[len(stk1):right]

                # print('2:', curr_len, right, curr)

                while len(stk2):
                    stk1.append(stk2.pop(-1))

            # print('2:', ans, max_len, stk1, stk2)

            stk1.append(s[curr])
            curr += 1

        return ans
        