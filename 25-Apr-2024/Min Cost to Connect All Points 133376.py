# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def find(components, idx):
            while components[idx] != idx:
                components[idx] = components[components[idx]]
                idx = components[idx]
            
            return idx
        
        def get_weighted_edges(points):
            n = len(points)
            edges = []

            for i in range(n):
                x1, y1 = points[i]

                for j in range(i+1, n):
                    x2, y2 = points[j]
                    # edge is represented by the idx of the points it conect and the cost of connecting
                    cost = abs(x1-x2) + abs(y1-y2)
                    edges.append((i, j, cost))
            
            return edges
        
        n = len(points)
        edges = get_weighted_edges(points)
        edges.sort(key = lambda edge: edge[-1]) # sort by weight
        components = [i for i in range(n)]

        min_cost = 0
        for i, j, cost in edges:
            group_of_i = find(components, i)
            group_of_j = find(components, j)

            if group_of_i != group_of_j:
                min_cost += cost
                components[group_of_i] = group_of_j
        
        return min_cost
