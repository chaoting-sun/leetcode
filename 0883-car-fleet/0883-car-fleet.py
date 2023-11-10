"""
position = 0 2 4
speed.   = 4 2 1

form car fleet (>=2): (前pos-後pos)/(後speed-前speed) >= target-前position
suppose that there are three cars in order: a, b, c
if b and c form a car fleet:
    check if a and c form a car fleet
else:
    check if a and b form a car fleet
"""

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = list(zip(position, speed))
        ps.sort(key=lambda x: x[0])
        position = [ps[i][0] for i in range(len(ps))]
        speed = [ps[i][1] for i in range(len(ps))]

        print(position)
        print(speed)

        nCarFleet = 1
        currSlow = len(position)-1

        for i in range(len(position)-2, -1, -1):
            if speed[i] <= speed[currSlow] or \
            (position[currSlow]-position[i]) / (speed[i]-speed[currSlow]) > (target-position[currSlow]) / speed[currSlow]:
                nCarFleet += 1 # the car_{i-1}
                currSlow = i
    
        return nCarFleet