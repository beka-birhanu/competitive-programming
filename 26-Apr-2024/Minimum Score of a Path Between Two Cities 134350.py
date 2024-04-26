# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:      
        def find(v):
            while parent[v] != v:
                parent[v] = parent[parent[v]] # path compression
                v = parent[v]
            return v
        
        parent = [i for i in range(n + 1)]

        for road in roads:
            v, u, dst = road
            p_v, p_u = find(v), find(u)
            parent[p_u] = p_v

        return min([d for v,u,d in roads if find(v) == find(1)])
