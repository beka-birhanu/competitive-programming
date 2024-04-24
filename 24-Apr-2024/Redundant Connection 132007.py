# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def collect(src, dest, colors, adj_list):
            last_removable = None
            st = [src]
            visited = set([src])

            while st:
                curr = st.pop()

                for nbr, place in adj_list[curr]:
                    

                    if colors[nbr] == 1:
                        if nbr not in visited:
                            st.append(nbr)
                            visited.add(nbr)

                        if not last_removable:
                            last_removable = [nbr+1, curr+1, place]

                        else:
                            last_removable = max(last_removable, [nbr+1, curr+1, place], key = lambda x : x[-1])
            
            return last_removable[:-1]

        def find(node, color, adj_list):
            for nbr, place in adj_list[node]:
                if colors[nbr] == 1:
                    # collect the path
                    # the maximum of the removable based on the possition in the edges
                    return collect(nbr, node, colors, adj_list)
                
                if colors[nbr] == 0:
                    colors[nbr] = 1
                    adj_list[nbr].remove((node, place))
                    removable = find(nbr, color, adj_list)

                    if removable:
                        return removable
            
            colors[node] = 2

            return []

        n = len(edges)
        adj_list = [set() for _ in range(n)]
        colors = [0]*n

        for i, (a, b) in enumerate(edges):
            a -= 1
            b -= 1
            adj_list[a].add((b, i))
            adj_list[b].add((a, i))
        

        for i in range(n):
            if colors[i] == 0:
                colors[i] = 1
                removable = find(i, colors, adj_list)

                for a, b in edges:
                    if a in removable and b in removable:
                        return [a, b]

        
