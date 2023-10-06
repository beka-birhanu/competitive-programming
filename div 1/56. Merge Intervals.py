# Runtime 9046ms and Memory 18.8mb
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


 # Runtime 135ms and Memory 21.32mb 
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        intervals.append([float("inf"),float("inf")])
        i = 1
        prev_s,prev_e = intervals[0][0],intervals[0][1]
        ans = []
        while i < len(intervals):
            s,e = intervals[i]
            if s <= prev_e <= e:
                prev_e = e
            elif prev_e > e:
                pass
            else:
                ans.append([prev_s,prev_e])
                prev_s,prev_e = s,e
            i += 1
        return ans
