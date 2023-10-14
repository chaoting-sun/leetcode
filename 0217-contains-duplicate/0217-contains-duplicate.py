class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
      rec = {}
      for n in nums:
        if n in rec:
          return True
        else:
          rec[n] = 1
      return False