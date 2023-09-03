class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        heapq.heapify(intervals)
        result = []
        while len(intervals) > 0:
            x,y =  heapq.heappop(intervals)
            while len(intervals) > 0:
                w,z = heapq.heappop(intervals)
                if w <= y <= z:
                    y = z
                elif y > z:
                    pass
                else:
                    heapq.heappush(intervals,[w,z])
                    heapq.heapify(intervals)
                    break
            result.append([x,y])
        return result
