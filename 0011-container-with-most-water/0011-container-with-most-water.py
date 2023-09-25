### method1: brute force (TLE)

# class Solution(object):
#     def maxArea(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         maxArea = 0

#         for i in range(len(height)-1):
#             for j in range(i+1, len(height)):
#                 area = (j-i) * min(height[i], height[j])
#                 maxArea = max(maxArea, area)
#         return maxArea


### method2: two pointer

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        maxArea = 0
        
        while l < r:
            currArea = min(height[l], height[r]) * (r - l)
            maxArea = max(maxArea, currArea)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxArea
        