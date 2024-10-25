# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        for i in range(len(heights)-1):
            h = heights[i+1] - heights[i]
            if h > 0 and len(heap) >= ladders:
               bricks -= heapq.heappushpop(heap,h)
               if bricks < 0:
                   return i
            elif h > 0:
                heapq.heappush(heap,h)
                
        return len(heights)-1