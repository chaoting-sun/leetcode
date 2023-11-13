class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        mem = defaultdict(list)
        
        for employ, time in access_times:
            mem[employ].append(int(time))
        
        ans = []
        
        for employ, timeList in mem.items():
            if len(timeList) < 3:
                continue

            timeList.sort()
            
            left, right = 0, 2
            
            while right < len(timeList):
                if timeList[right] - timeList[left] < 100:
                    ans.append(employ)
                    break
                else:
                    right += 1
                    left += 1
        return ans