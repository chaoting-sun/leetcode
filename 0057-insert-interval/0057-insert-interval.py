### method1

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)

        if n == 0:
            return [newInterval]
        
        head = 0
        tail = n - 1
        ans = []

        while head < n and newInterval[0] > intervals[head][1]:
            head += 1

        while tail >= 0 and newInterval[1] < intervals[tail][0]:
            tail -= 1

        # left
        if head > 0:
            ans = ans + intervals[:head]
        
        # center
        if head == n:
            ans = ans + [newInterval]
        elif tail == -1:
            ans = [newInterval] + ans
        else:
            ans = ans + [[min(intervals[head][0], newInterval[0]), max(intervals[tail][1], newInterval[1])]]
        
        # right
        if tail + 1 < n:
            ans = ans + intervals[tail+1:]

        return ans


### method2

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []

        i = 0
        n = len(intervals)

        while i < n:
            if intervals[i][1] < newInterval[0]: # left
                ans.append(intervals[i])
            elif intervals[i][0] > newInterval[1]: # right
                break
            else: # center
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        ans.append(newInterval)

        while i < n:
            ans.append(intervals[i])
            i += 1
        return ans