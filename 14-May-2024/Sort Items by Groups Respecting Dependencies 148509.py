# Problem: Sort Items by Groups Respecting Dependencies - https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        groups = [[] for _ in range(n+m)]
        group_graph = [[] for _ in range(n+m)]
        group_in_degree = [0]*(n+m)
        
        indev_graph = [[] for _ in range(n)]
        indev_in_degree = [0]*n

        id = m
        for i, g in enumerate(group):
            if g >= 0:
                groups[g].append(i)
            
            else:
                groups[id].append(i)
                group[i] = id
                id += 1

        for i, items in enumerate(beforeItems):
            for item in items:
                if group[i] == group[item]:
                    indev_in_degree[i] += 1
                    indev_graph[item].append(i)
                
                else:
                    group_graph[group[item]].append(group[i])
                    group_in_degree[group[i]] += 1
        
        # sort groups               
        q = deque()
        for i in range(id):
            if group_in_degree[i] == 0:
                q.append(i)
        
        group_sort = []
        while q:
            curr = q.popleft()
            group_sort.append(curr)

            for nbr in group_graph[curr]:
                group_in_degree[nbr] -= 1
                
                if group_in_degree[nbr] == 0:
                    q.append(nbr)

        if len(group_sort) != id:
            return []
        
        # sort indididuals in each group
        indev_sort = []
        for g in group_sort:
            q = deque()
            for member in groups[g]:
                if indev_in_degree[member] == 0:
                    q.append(member)

            while q:
                curr = q.popleft()
                indev_sort.append(curr)

                for nbr in indev_graph[curr]:
                    indev_in_degree[nbr] -= 1
                    
                    if indev_in_degree[nbr] == 0:
                        q.append(nbr)

        return indev_sort if len(indev_sort) == n else []