# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parents = [i for i in range(n)]

        def find_parent(parents, node):
            while parents[node] != node:
                parents[node] = parents[parents[node]]
                node = parents[node]
            
            return node
        
        for a, b in edges:
            parent_of_a = find_parent(parents, a-1)
            parent_of_b = find_parent(parents, b-1)

            if parent_of_a == parent_of_b:
                return [a, b]
            
            parents[parent_of_a] = parent_of_b




            

        
