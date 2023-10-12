### method1: hash table

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        m = defaultdict(int)
        
        for num in nums:
            m[num] += 1

        n //= 2
        for k, v in m.items():
            if v > n:
                return k
        return 0


# ### method2: collections.Counter

# from collections import Counter
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         counts = Counter(nums)
#         return max(counts, key=counts.get)