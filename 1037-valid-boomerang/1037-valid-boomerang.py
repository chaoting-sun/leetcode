class Solution:
    def isDistinct(self, p1: List[int], p2: List[int]) -> bool:
        return not (p1[0] == p2[0] and p1[1] == p2[1])
    
    def isVerticallyAligned(self, p1: List[int], p2: List[int], p3: List[int]):
        return p1[0] == p2[0] and p2[0] == p3[0]

    def isHorizontallyAligned(self, p1: List[int], p2: List[int], p3: List[int]):
        return p1[1] == p2[1] and p2[1] == p3[1]

    def isAlignedWithSlope(self, p1: List[int], p2: List[int], p3: List[int]):
        ratio1 = (p1[0] - p2[0]) / (p1[1] - p2[1])
        ratio2 = (p1[0] - p3[0]) / (p1[1] - p3[1])
        return ratio1 != ratio2

    def isBoomerang(self, points: List[List[int]]) -> bool:
        p1 = points[0]
        p2 = points[1]
        p3 = points[2]

        if not (self.isDistinct(p1, p2) and self.isDistinct(p2, p3) and self.isDistinct(p3, p1)):
            return False

        if p1[0] == p2[0] or p2[0] == p3[0] or p3[0] == p1[0]:
            return not self.isVerticallyAligned(p1, p2, p3)
        
        if p1[1] == p2[1] or p2[1] == p3[1] or p3[1] == p1[1]:
            return not self.isHorizontallyAligned(p1, p2, p3)

        return self.isAlignedWithSlope(p1, p2, p3)


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        p1 = points[0]
        p2 = points[1]
        p3 = points[2]

        return (p1[0] - p2[0]) * (p1[1] - p3[1]) != (p1[1] - p2[1]) * (p1[0] - p3[0])