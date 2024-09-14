# Problem: Minimum Time Difference - https://leetcode.com/problems/minimum-time-difference/

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        timePoints = list(map(lambda x: tuple(map(int, x.split(":"))), timePoints)) #changing time points int tuple of (h, m)
        min_def = float('inf')
        
        for i in range( len(timePoints)-1 ):
            (h1,m1), (h2, m2) = timePoints[i], timePoints[i+1]

            min_def = min(60*(h2 - h1) + (m2 - m1), min_def)

        (h1,m1), (h2, m2) = timePoints[0], timePoints[-1]
        min_def = min(60*(24 + h1 -h2) + (m1 - m2), min_def)

        return min_def
