# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        self.srt = SortedList()

    def addNum(self, num: int) -> None:
        self.srt.add(num)

    def findMedian(self) -> float:
        return median(self.srt)
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()