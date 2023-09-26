class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pairs = { ')': '(',
                  ']': '[',
                  '}': '{' }

        p = 0
        stk = []

        while p < len(s):
            if s[p] in ')]}':
                if len(stk) > 0 and stk[-1] == pairs[s[p]]:
                    stk.pop()
                    p += 1
                else:
                    return False
            else:
                stk.append(s[p])
                p += 1
        if len(stk) > 0:
            return False
        return True
                