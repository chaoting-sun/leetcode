class MedianFinder:
    def __init__(self):
        self.maxheap = [] # for small values
        self.minheap = [] # for large values

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxheap, -num)

        # check if max. value in maxheap is smaller than min. value in minheap
        if self.maxheap and self.minheap and -self.maxheap[0] > self.minheap[0]:
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
        
        # check if the number of elements on both heaps are even
        if len(self.maxheap) - 1 > len(self.minheap):
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
        if len(self.minheap) - 1 > len(self.maxheap):
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))

    def findMedian(self) -> float:
        if len(self.maxheap) > len(self.minheap):
            return -self.maxheap[0]
        if len(self.maxheap) < len(self.minheap):
            return self.minheap[0]
        return (-self.maxheap[0] + self.minheap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


# cleaner code:
# 1. https://leetcode.com/problems/find-median-from-data-stream/solutions/411354/two-heap-approach-with-python-o-log-n-insert-o-1-median/?envType=list&envId=rab78cw1
# 2. https://leetcode.com/problems/find-median-from-data-stream/solutions/696658/python-logic-explained-with-2-heaps-clean-code/?envType=list&envId=rab78cw1