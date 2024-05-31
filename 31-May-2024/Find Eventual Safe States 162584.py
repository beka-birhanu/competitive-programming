# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def checkSafety(colors, graph, node, ans):
            for nbr in graph[node]:
                if colors[nbr] == 0:
                    colors[nbr] = 1
                    checkSafety(colors, graph, nbr, ans)

                if colors[nbr] == 1:
                    return None
            
            colors[node] = 2
            ans.append(node)

            return None
        
        n = len(graph)
        colors = [0]*n
        ans = []

        for node in range(n):
            if colors[node] == 0:
                colors[node] = 1
                checkSafety(colors, graph, node, ans)
        
        ans.sort()
        return ans
