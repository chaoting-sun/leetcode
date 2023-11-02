# method: bit manipulation

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res <<= 1

            # res = res | (n & 1)
            if n & 1 == 1:
                res += 1
            
            n >>= 1
        return res


# method: fast bit manipulation
# source: https://www.youtube.com/watch?v=-5z9dimxxmI

class Solution:
    def reverseBits(self, n: int) -> int:
        n = (n >> 16) | (n << 16);
        n = (n & 0xff00ff00) >> 8 | (n & 0x00ff00ff) << 8
        n = (n & 0xf0f0f0f0) >> 4 | (n & 0x0f0f0f0f) << 4
        n = (n & 0xcccccccc) >> 2 | (n & 0x33333333) << 2
        n = (n & 0xaaaaaaaa) >> 1 | (n & 0x55555555) << 1
        return n