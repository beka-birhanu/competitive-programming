# Problem: Divide intervals into minimum number of groups - https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        minHeap = []
        intervals.sort()

        for it in intervals:
            if minHeap and minHeap[0] < it[0]:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, it[1])

        return len(minHeap)