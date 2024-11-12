class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        isXdirOverlapped = rec1[2] > rec2[0] and rec2[2] > rec1[0]
        isYdirOverlapped = rec1[3] > rec2[1] and rec2[3] > rec1[1]
        return isXdirOverlapped and isYdirOverlapped