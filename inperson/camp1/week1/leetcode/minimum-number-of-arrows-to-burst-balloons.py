class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        arrows_shot = 0
        pos = 0
        while pos < len(points):
            last_possible_pos = points[pos][1]
            while pos < len(points) and last_possible_pos >= points[pos][0]:
                last_possible_pos = min(points[pos][1] , last_possible_pos)
                pos += 1
            arrows_shot += 1
        return arrows_shot