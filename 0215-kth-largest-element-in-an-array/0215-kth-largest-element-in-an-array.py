### method1: sort

# time complexity: O(NlgN)
# space complexity: O(1)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k-1]


### method2: heap (priority queue)

# time complexity: O(N lgk) (in the worst case, the values in nums are in increasing order)
# space complexity: O(N)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = []
        for n in nums:
            if len(minheap) < k:
                heapq.heappush(minheap, n)
            elif minheap[0] < n:
                heapq.heappop(minheap)
                heapq.heappush(minheap, n)
        return minheap[0]


### method3: quick select

# source: https://leetcode.com/problems/kth-largest-element-in-an-array/solutions/1019513/python-quickselect-average-o-n-explained/?envType=list&envId=rr2ss0g5
# time complexity: O(N) on average
# space complexity: O(N)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = nums[0]
        left, mid, right = [], [], []

        for n in nums:
            if n < pivot:
                right.append(n)
            elif n > pivot:
                left.append(n)
            else:
                mid.append(n)
        
        if k <= len(left):
            return self.findKthLargest(left, k)
        elif k > len(left) + len(mid):
            return self.findKthLargest(right, k-len(left)-len(mid))
        else:
            return pivot

### method3.1: quick select by swapping (TLE)

# class Solution:
#     def quickSelect(self, nums, left, right):
#         pivot = nums[right]
#         i = left
#         for j in range(left, right):
#             if nums[j] >= pivot:
#                 nums[i], nums[j] = nums[j], nums[i]
#                 i += 1
#         nums[i], nums[right] = nums[right], nums[i]
#         return i
        
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         left, right = 0, len(nums)-1
        
#         while True:
#             i = self.quickSelect(nums, left, right)
#             if i > k-1:
#                 right = i-1
#             elif i < k-1:
#                 left = i+1
#             else:
#                 break
        
#         return nums[k-1]