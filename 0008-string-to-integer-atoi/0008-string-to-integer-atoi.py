import numpy as np

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        valid_char = ['0', '1', '2', '3', '4',
                      '5', '6', '7', '8', '9']

        sign = 0
        ptr = 0

        while ptr < len(s):
            print(ptr, s[ptr])

            if s[ptr] == ' ':
                if sign != 0:
                    return 0
                ptr += 1
                continue
            elif s[ptr] == '+' or s[ptr] == '-':
                if sign == 0:
                    sign = 1 if s[ptr] == '+' else -1
                else:
                    return 0
                ptr += 1
                continue
            elif s[ptr] in valid_char:
                break
            else: # other character
                return 0

        digits = []

        for i in range(ptr, len(s)):
            try:
                digits.append(int(s[i]))
            except:
                break

        mysum = 0
        ub = 2**31-1
        lb = -2**31

        for i in range(len(digits)):
            mysum += digits[i] * 10**(len(digits)-i-1)

        mysum = sign*mysum if sign == -1 else mysum

        if mysum > ub:
            return ub
        elif mysum < lb:
            return lb
        else:
            return mysum


        

            



            
            
                
            
        