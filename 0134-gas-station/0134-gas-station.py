# source: https://leetcode.com/problems/gas-station/description/?envType=list&envId=rr2ss0g5
# time complexity: O(N)
# space complexity: O(N)

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        total = 0
        debt = 0
        for i in range(len(gas)):
            debt += gas[i] - cost[i]
            total += gas[i] - cost[i]
            if debt < 0:
                start = i+1
                debt = 0
        return -1 if total < 0 else start