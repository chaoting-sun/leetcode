import numpy as np

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        prefixMax = np.zeros((n,), dtype=np.int)
        suffixMax = np.zeros((n,), dtype=np.int)
        
        maxV = 0
        for i in range(n):
            maxV = max(maxV, height[i])
            prefixMax[i] = maxV
        maxV = 0
        for i in range(n-1, -1, -1):
            maxV = max(maxV, height[i])
            suffixMax[i] = maxV

        vol = 0
        for i in range(n):
            vol += min(prefixMax[i], suffixMax[i]) - height[i]

        return vol


# class Solution(object):
#     def trap(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         vol = 0
#         n = len(height)

#         if n == 1 or n == 2:
#             return 0

#         l = mid = r = 1

#         while mid < n - 1:
#             hmax = height[mid]
#             while l > 0 and height[l-1] > height[l]:
#                 l -= 1
#             while r < n - 1 and height[r] < height[r+1]:
#                 r += 1
#             hmax = max(hmax, height[l], height[r])

#             print(l, mid, r, hmax)

#             if hmax == height[mid]:
#                 mid += 1
#                 l = r = mid
#             else:
#                 hmin = min(height[l], height[r])
#                 print('hmin:', hmin)
#                 for i in range(l+1, r):
#                     vol += (hmin - height[i])
#                 l = r = mid = r + 1
#             print(vol)
#         return vol


            
        


        