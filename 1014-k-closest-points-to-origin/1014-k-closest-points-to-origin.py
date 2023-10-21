from numpy import argsort

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis = [x**2+y**2 for x, y in points]
        smallIndices = argsort(dis)[:k]
        return [points[i] for i in smallIndices]