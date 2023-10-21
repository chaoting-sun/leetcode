### method: dynamic programming (weighted interval scheduling)

# time complexity: O(NlogN) (sort by finish time)
# space complexity: O(N)

from numpy import argsort
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)

        # a good way:
        # jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])

        sorted_ids = argsort(endTime)
        startTime = [startTime[i] for i in sorted_ids]
        endTime = [endTime[i] for i in sorted_ids]
        profit = [profit[i] for i in sorted_ids]

        p = [-1] * n
        for i in range(1, n):
            for j in range(i-1, -1, -1):
                if endTime[j] <= startTime[i]:
                    p[i] = j
                    break

        opt = [0] * (n+1)

        for i in range(1, n+1):
            profitWithCurr = profit[i-1]
            if p[i-1] != -1:
                profitWithCurr += opt[p[i-1]+1]
            opt[i] = max(profitWithCurr, opt[i-1])
        return opt[n]