### method1: sort

# time complexity: O(nlogn)
# space complexity: O(n)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                i += 2
            else:
                return nums[i]
        return nums[i]


### method2: hash table

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        st = set()
        for n in nums:
            if n in st:
                st.remove(n)
            else:
                st.add(n)
        return st.pop()