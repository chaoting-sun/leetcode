### method1: mine

import numpy as np

class Solution:
    def myAtoi(self, s: str) -> int:
        valid_char = ['0', '1', '2', '3', '4',
                      '5', '6', '7', '8', '9']
        sign = 0
        p = 0

        while p < len(s):
            if s[p] == ' ':
                if sign != 0:
                    return 0
                p += 1
                continue
            elif s[p] == '+' or s[p] == '-':
                if sign == 0:
                    sign = 1 if s[p] == '+' else -1
                else:
                    return 0
                p += 1
                continue
            elif s[p] in valid_char:
                break
            else: # other character
                return 0

        digits = []

        for i in range(p, len(s)):
            try:
                digits.append(int(s[i]))
            except:
                break

        ans = 0
        ub = 2**31-1
        lb = -2**31

        for i in range(len(digits)):
            ans += digits[i] * 10**(len(digits)-i-1)

        ans = sign*ans if sign == -1 else ans

        if ans > ub:
            return ub
        elif ans < lb:
            return lb
        else:
            return ans


### method2: faster

class Solution:
    def myAtoi(self, s: str) -> int:
        p = 0
        n = len(s)

        while p < n and s[p] == ' ':
            p += 1
        
        positive = 0
        negative = 0

        if p < n and s[p] == '+':
            positive = 1
            p += 1
        
        if p < n and s[p] == '-':
            negative = 1
            p += 1
        
        ans = 0

        while p < n and '0' <= s[p] <= '9':
            ans = ans * 10 + (ord(s[p]) - ord('0'))
            p += 1

        if negative == 1:
            ans *= -1

        if positive == 1 and negative == 1:
            return 0

        ub = 2**31 - 1
        lb = - 2**31

        if ans > ub:
            return ub
        elif ans < lb:
            return lb
        else:
            return ans