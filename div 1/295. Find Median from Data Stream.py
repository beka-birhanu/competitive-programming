# Runtime 399 ms and Memory38.5 MB
class MedianFinder:
    def __init__(self):
        self.left = []
        self.right= []

    def addNum(self, num: int) -> None:
        if len(self.left) == len(self.right):
            if len(self.right) and self.right[0] < num:
                heapq.heappush(self.left,-1*heapq.heapreplace(self.right, num))
            else:
                heapq.heappush(self.left,-1*num)
        else:
            if len(self.left) and self.left[0] * -1 > num:
                heapq.heappush(self.right,-1*heapq.heapreplace(self.left, -1*num))
            else:
                heapq.heappush(self.right,num)
    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-1*self.left[0] + self.right[0])/2
        else:
            return -1*self.left[0]

# Runtime 5412 ms and Memory 38.1 MB

class MedianFinder2:
    def __init__(self):
        self.lst = []
        self.sorted = False

    def addNum(self, num: int) -> None:
        self.lst.append(num)
        self.sorted = False
    def findMedian(self) -> float:
        if self.sorted:
            return median(self.lst)
        else:
            self.lst.sort()
            self.sorted = True
            return median(self.lst)
