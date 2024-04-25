# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        # the min distance it takes to reach a point
        distances = [[inf, i] for i in range(n)]
        # the first point can be reached with 0 distance
        distances[0][0] = 0
        min_cost = 0

        while distances:
            closest = min(distances)
            min_cost += closest[0]
            x1, y1 = points[closest[1]]

            closest[:] = distances[-1][:]
            distances.pop()

            for distance in distances:
                x2, y2 = points[distance[1]]
                distance[0] = min(distance[0], abs(x1 - x2) + abs(y1 - y2))
        
        return min_cost

