### method1: sort

# time complexity: O(nlogn)
# space complexity: O(1)

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

# time complexity: O(n)
# space complexity: O(n)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        st = set()
        for n in nums:
            if n in st:
                st.remove(n)
            else:
                st.add(n)
        return st.pop()


### method3: bit manipulation (XOR)

# source: https://leetcode.com/problems/single-number/solutions/1771720/c-easy-solutions-sorting-xor-maps-or-frequency-array/?envType=list&envId=rr2ss0g5
# time complexity: O(n)
# space complexity: O(1)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for n in nums:
            ans ^= n
            print(ans)
        return ans