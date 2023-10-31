class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        xmax = ymax = zmax = 0
        for x, y, z in triplets:
            if x > target[0] or y > target[1] or z > target[2]:
                continue
            if x < target[0] and y < target[1] and z < target[2]:
                continue
            
            xmax = max(xmax, x)
            ymax = max(ymax, y)
            zmax = max(zmax, z)
        
        return xmax == target[0] and ymax == target[1] and zmax == target[2]