class MedianFinder:

    def __init__(self):
        self.mnheap = [] # stores the second half
        self.mxheap = [] # stores the first half

    def addNum(self, num: int) -> None:
        v = heappushpop(self.mxheap, -num)
        heappush(self.mnheap, -v)

        if len(self.mnheap) > len(self.mxheap):
            v = heappop(self.mnheap)
            heappush(self.mxheap, -1 * v)

    def findMedian(self) -> float:
        if len(self.mxheap) > len(self.mnheap):
            return -1 * self.mxheap[0]
        else:
            return (self.mnheap[0] - self.mxheap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()