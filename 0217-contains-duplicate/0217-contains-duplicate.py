class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
      rec = {}
      for n in nums:
        if n in rec:
          rec[n] += 1
        else:
          rec[n] = 1
      for v in rec.values():
        if v >= 2:
          return True
      return False