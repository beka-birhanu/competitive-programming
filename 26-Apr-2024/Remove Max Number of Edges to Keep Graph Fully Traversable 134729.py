# Problem: Remove Max Number of Edges to Keep Graph Fully Traversable - https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        def find(parents, i):
            while i != parents[i]:
                parents[i] = parents[parents[i]]
                i = parents[i]
            
            return i
        
        alice = [i for i in range(n)]
        bob = [i for i in range(n)]
        removable = 0
        edges.sort(reverse = True)

        for t, u, v in edges:
            u -= 1
            v -= 1
            used = False
            
            if t == 1 or t == 3:
                p_u = find(alice, u)
                p_v = find(alice, v)

                if p_u != p_v:
                    used = True
                
                alice[p_u] = p_v 

            if t == 2 or t == 3:
                p_u = find(bob, u)
                p_v = find(bob, v)

                if p_u != p_v:
                    used = True

                bob[p_u] = p_v  

            if not used:
                removable += 1


        alice_components = len(set(find(alice, i) for i in range(n)))
        if alice_components > 1:
            return -1

        bob_components = len(set(find(bob, i) for i in range(n)))
        if bob_components > 1:
            return -1
        
        return removable
