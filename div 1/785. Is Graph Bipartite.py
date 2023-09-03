class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def check(u):
            color[u] = -1
            stack = [u]
            while stack:
                u = stack.pop()
                for v in graph[u]:
                    if color[v] == 0:
                        if color[u] == 1:
                            color[v] = -1
                        else:
                            color[v] = 1
                        stack.append(v)
                    elif color[v] == color[u]:
                        return False
            return True

        color = [0]*len(graph)
        for u in range(len(graph)):
            if color[u] == 0 and not check(u):
                return False
               
        return True

