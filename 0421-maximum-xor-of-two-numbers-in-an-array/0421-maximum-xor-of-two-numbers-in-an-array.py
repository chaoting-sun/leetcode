### method1: trie

class Solution:
    def __init__(self):
        self.trie = {}

    def findMaximumXOR(self, nums: List[int]) -> int:
        for num in nums:
            node = self.trie
            for i in range(31,-1,-1):
                bit = num>>i & 1
                if bit not in node:
                    node[bit] = {}
                node = node[bit]
        
        maxXor = float('-inf')

        for num in nums:
            node = self.trie
            xor = 0
            for i in range(31,-1,-1):
                opposite_bit = 1 - (num>>i) & 1
                if opposite_bit in node:
                    xor = xor | 1<<i
                    node = node[opposite_bit]
                else:
                    node = node[1-opposite_bit]
            maxXor = max(maxXor, xor)
        
        return maxXor


### method2: prefix
# nice explanation: https://juejin.cn/post/6957251700885307400?from=search-suggest
# time complexity: O(N)
# space complexity: O(N)

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        res = 0
        mask = 0

        for i in range(31, -1, -1):
            mask = mask | (1 << i)
            
            prefixes = set()
            for num in nums:
                prefixes.add(num & mask)
            
            wantBe = res | 1 << i
            for p1 in prefixes:
                p2 = p1 ^ wantBe
                if p2 in prefixes:
                    res = wantBe
                    break
        return res