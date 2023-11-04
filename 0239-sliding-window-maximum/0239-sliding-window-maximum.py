### method1: deque

# time complexity: O(N)
# space complexity: O(N)

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        maxv = float('-inf')

        for i in range(k):
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)
            maxv = max(maxv, nums[i])
        
        ans = [maxv]

        for i in range(k, len(nums)):
            # pop out the values smaller than nums[i]
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            # if all values are popped out, nums[i] is the largest value
            if not q:
                maxv = max(maxv, nums[i])
            
            q.append(i)
            
            if q[0] == i-k:
                q.popleft()
                maxv = nums[q[0]]
            
            ans.append(maxv)
        return ans