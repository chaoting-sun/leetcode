### method1: hashtable

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n_chars = {}
        for i in range(len(nums)):
            if nums[i] in n_chars:
                n_chars[nums[i]] += 1
            else:
                n_chars[nums[i]] = 1
        max_k, max_v = 0, 0
        for k, v in n_chars.items():
            if v > max_v:
                max_k, max_v = k, v
        return max_k


### method2: counter

from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        return max(counts, key=counts.get)