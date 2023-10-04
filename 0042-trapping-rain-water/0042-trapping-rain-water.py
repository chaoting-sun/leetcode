# method1: dp

# class Solution(object):
#     def trap(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         n = len(height)
#         prefixMax = [0] * n
#         suffixMax = [0] * n
        
#         maxV = 0
#         for i in range(n):
#             maxV = max(maxV, height[i])
#             prefixMax[i] = maxV
#         maxV = 0
#         for i in range(n-1, -1, -1):
#             maxV = max(maxV, height[i])
#             suffixMax[i] = maxV

#         vol = 0
#         for h, pref, suff in zip(height, prefixMax, suffixMax):
#             vol += min(pref, suff) - h
#         return vol


# method2: two pointers

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        leftMax = rightMax = 0
        vol = 0

        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])

            if leftMax > rightMax:
                vol += rightMax - height[right]
                right -= 1
            else:
                vol += leftMax - height[left]
                left += 1
        return vol


            
        


        