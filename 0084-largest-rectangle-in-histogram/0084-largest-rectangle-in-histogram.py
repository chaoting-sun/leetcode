### method1: stack (time complexity=O(N); space complexity=O(N))

# https://leetcode.com/problems/largest-rectangle-in-histogram/solutions/28917/ac-python-clean-solution-using-stack-76ms/?envType=list&envId=rab78cw1

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = [-1]
        heights.append(0)

        for i in range(len(heights)):
            while heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        heights.pop()
        return ans


### method2: dp (time complexity=?; space complexity=O(N))

# https://leetcode.com/problems/largest-rectangle-in-histogram/solutions/28902/5ms-o-n-java-solution-explained-beats-96/?envType=list&envId=rab78cw1

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        lessFromLeft = [-1] * n
        lessFromRight = [n] * n

        
        for i in range(1, n):
            p = i - 1
            while p >= 0 and heights[p] >= heights[i]:
                p = lessFromLeft[p]
            lessFromLeft[i] = p
        
        for i in range(n-2, -1, -1):
            p = i + 1
            while p < n and heights[i] <= heights[p]:
                p = lessFromRight[p]
            lessFromRight[i] = p

        ans = 0
        for i in range(n):
            ans = max(ans, heights[i] * (lessFromRight[i]-lessFromLeft[i]-1))
        return ans