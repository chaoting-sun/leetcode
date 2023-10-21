### mine

class Solution(object):
    def addBinary(self, a: str, b: str) -> str:
        ans = ''
        i, j = len(a)-1, len(b)-1
        tmp = 0

        while i >= 0 or j >= 0:
            print(i, j)
            if i < 0:
               tmp += int(b[j])
               j -= 1
            elif j < 0:
                tmp += int(a[i])
                i -= 1
            else:
                tmp += int(a[i]) + int(b[j])
                i -= 1
                j -= 1
            
            if tmp == 0:
                ans = '0' + ans
            elif tmp == 1:
                ans = '1' + ans
                tmp = 0
            elif tmp == 2:
                ans = '0' + ans
                tmp = 1
            elif tmp == 3:
                ans = '1' + ans
                tmp = 1

        if tmp == 1:
            return '1' + ans
        else:
            return ans


### cleaner

class Solution(object):
    def addBinary(self, a: str, b: str) -> str:
        ans = []
        i, j = len(a)-1, len(b)-1
        carry = 0

        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            ans.append(str(carry % 2))
            carry //= 2
        return ''.join(ans[::-1])