### method1: hash table

# time complexity: O(N)
# space complexity: O(N)

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


### method2: sorting

# time complexity: O(NlogN)
# space complexity: O(1)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]


### Boyer-Moore Majority Vote Algorithm

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major = nums[0]
        count = 1

        for i in range(1, len(nums)):
            if count == 0:
                major = nums[i]
                count += 1
            elif nums[i] == major:
                count += 1
            else:
                count -= 1
        return major