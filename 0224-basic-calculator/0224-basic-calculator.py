### method: stack (so hard)

# helpful source: https://www.youtube.com/watch?v=081AqOuasw0

# time complexity: O(N)
# space complexity: O(N)

class Solution:
    def calculate(self, s: str) -> int:
        sign = 1 # 1 or -1
        res = 0
        stk = []

        i = 0
        while i < len(s): 
            if s[i].isdigit():
                num = 0
                j = i
                while j < len(s) and s[j].isdigit():
                    num = num * 10 + int(s[j])
                    j += 1
                res += sign * num
                i = j - 1
            elif s[i] == '+':
                sign = 1
            elif s[i] == '-':
                sign = -1
            elif s[i] == '(':
                # if we find (, then we start a new calculation
                # so we store the previous res and sign in the stack
                stk.append(res)
                stk.append(sign)
                res = 0
                sign = 1
            elif s[i] == ')':
                # if we find ), then we stop current calculation
                # in the same parenthesis level
                res *= stk.pop() # previous sign
                res += stk.pop() # previous result
            i += 1
        return res