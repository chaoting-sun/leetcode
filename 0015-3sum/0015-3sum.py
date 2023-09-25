# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         nums.sort()
#         ans = []

#         for c in range(1, len(nums)-1):
#             l = 0
#             r = len(nums) - 1

#             while l < c and c < r:
#                 val3 = [nums[l], nums[c], nums[r]]
#                 sum3 = sum(val3)
#                 if sum3 > 0:
#                     r -= 1
#                 elif sum3 < 0:
#                     l += 1
#                 else:
#                     if val3 not in ans:
#                         ans.append(val3)
                    
#                     if abs(nums[l]) > abs(nums[r]):
#                         l += 1
#                     else:
#                         r -= 1
#         return ans


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []

        print(nums)

        for l in range(0, len(nums)-2):
            c = l + 1
            r = len(nums) - 1
            
            if l > 0 and nums[l] == nums[l-1]:
                continue

            while c < r:
                val3 = [nums[l], nums[c], nums[r]]
                sum3 = sum(val3)
                if sum3 > 0:
                    r -= 1
                elif sum3 < 0:
                    c += 1
                else:
                    ans.append(val3)
                    
                    while c < r and nums[c] == val3[1]:
                        c += 1
                    while c < r and nums[r] == val3[2]:
                        r -= 1
        return ans

