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

        