class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = [-1] * len(intervals)
        for idx,interval in enumerate(intervals):
            starts[idx] = (interval[0],idx)
        
        starts.sort()
    
        for idx in range(len(intervals)):
            end = intervals[idx][1]
            l,r = 0, len(intervals)-1

            while l < r:
                mid = l + (r-l)//2
                if starts[mid][0] >= end:
                    r = mid
                else:
                    l = mid + 1
                    
            intervals[idx] =  starts[r][1] if starts[r][0] >= end else -1 

        return intervals