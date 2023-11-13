# time complexity: O(N)
# space complexity: O(1)

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        
        ans1 = 0
        i = n-2
        max1, max2 = nums1[n-1], nums2[n-1]        
        
        while i >= 0:
            if nums1[i] > max1 or nums2[i] > max2:
                if nums1[i] > max2 or nums2[i] > max1:
                    return -1
                ans1 += 1
            i -= 1
    
        nums1[n-1], nums2[n-1] = nums2[n-1], nums1[n-1]
        
        ans2 = 1
        i = n-2
        max1, max2 = nums1[n-1], nums2[n-1]        
        
        while i >= 0:
            if nums1[i] > max1 or nums2[i] > max2:
                if nums1[i] > max2 or nums2[i] > max1:
                    return -1
                ans2 += 1
            i -= 1

        return min(ans1, ans2)