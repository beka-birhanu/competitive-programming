# Problem: Process Restricted Friend Requests - https://leetcode.com/problems/process-restricted-friend-requests/

from typing import List

class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        
        def find(parent: List[int], member: int) -> int:
            while member != parent[parent[member]]:
                parent[member] = parent[parent[member]]
                member = parent[member]
            return member

        def can_merge(root_u: int, root_v: int, parent: List[int], restrictions: List[set], n: int) -> bool:
            if root_u == root_v:
                return True

            for i in range(n):
                root_i = find(parent, i)
                if root_i == root_v and i in restrictions[root_u]:
                    return False
                if root_i == root_u and i in restrictions[root_v]:
                    return False
            return True

        parent = list(range(n))
        group_restrictions = [set() for _ in range(n)]
        
        for x, y in restrictions:
            group_restrictions[x].add(y)
            group_restrictions[y].add(x)
        
        results = []
        
        for u, v in requests:
            root_u = find(parent, u)
            root_v = find(parent, v)

            if can_merge(root_u, root_v, parent, group_restrictions, n):
                parent[root_u] = root_v
                group_restrictions[root_v].update(group_restrictions[root_u])
                results.append(True)
            else:
                results.append(False)
        
        return results
