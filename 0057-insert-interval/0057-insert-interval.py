class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
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
        print(head, tail)

        if head > 0:
            ans = ans + intervals[:head]
        
        if head == n:
            ans = ans + [newInterval]
        elif tail == -1:
            ans = [newInterval] + ans
        else:
            ans = ans + [[min(intervals[head][0], newInterval[0]), max(intervals[tail][1], newInterval[1])]]
        
        if tail + 1 < n:
            ans = ans + intervals[tail+1:]

        return ans