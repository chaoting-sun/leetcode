### method: bit manipulation

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for i in range(32):
            # get the least significant bit (LSB)
            res += n & 1
            # right shift
            n >>= 1
        return res