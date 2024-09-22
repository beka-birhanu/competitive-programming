# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1]*n
        
        for i in range(n):
            if color[i] == -1:
                color[i] = 1
                st = [i]

                while st:
                    vertex = st.pop()

                    for neighboure in graph[vertex]:
                        if color[neighboure] == -1:
                            color[neighboure] = abs(color[vertex]-1)
                            st.append(neighboure)
                        
                        elif color[neighboure] == color[vertex]:
                            return False
        
        return True