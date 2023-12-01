# time complexity: O(N)
# space complexity: O(1)

class Solution:
    def numberOfWays(self, corridor: str) -> int:
        ans = 1
        seatCnt = 0
        plantCnt = 0
        totalSeatCnt = 0

        for i in range(len(corridor)):
            if corridor[i] == 'S': # seat
                totalSeatCnt += 1

                if seatCnt < 2:
                    seatCnt += 1
                else:
                    ans *= plantCnt + 1
                    ans %= 10**9 + 7
                    plantCnt = 0
                    seatCnt = 1
            else: # plant
                if seatCnt == 2:
                    plantCnt += 1
        
        if totalSeatCnt < 2 or totalSeatCnt % 2 == 1:
            return 0
        return ans