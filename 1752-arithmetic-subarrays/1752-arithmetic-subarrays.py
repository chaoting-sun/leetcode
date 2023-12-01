### method1: sort
# time: O(m*n*lgn)
# space: O(n)

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = [True] * len(l)

        for i in range(len(l)):
            numsSorted = sorted(nums[l[i]:r[i]+1])
            interval = numsSorted[1] - numsSorted[0]
            
            for j in range(1, len(numsSorted)):
                if numsSorted[j] - numsSorted[j-1] != interval:
                    ans[i] = False
                    break
        return ans


### count patterns

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = [True] * len(l)
        
        for i in range(len(l)):
            minv, maxv = 10**6, -10**6
            for j in range(l[i], r[i]+1):
                if nums[j] < minv: minv = nums[j]
                if nums[j] > maxv: maxv = nums[j]
            
            subN = r[i] - l[i] + 1
            dist, mod = divmod(maxv-minv, subN-1)

            if minv == maxv:
                continue
            elif mod:
                ans[i] = False
            else:
                existed = [False] * subN
                for j in range(l[i], r[i]+1):
                    if (nums[j]-minv)%dist or existed[(nums[j]-minv)//dist]:
                        ans[i] = False
                        break
                    existed[(nums[j]-minv)//dist] = True
        return ans