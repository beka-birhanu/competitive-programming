# Problem: Count Unreachable Pairs of Nodes in an Undirected Graph - https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        def find(member):
            while member != groups[member]:
                groups[member] = groups[groups[member]]
                member = groups[member]
            
            return member

        groups = [i for i in range(n)]

        for a, b in edges:
            group_a = find(a)
            group_b = find(b)
            groups[group_b] = group_a
        
        counts = Counter(map(find, range(n))).values()
        unreachable_count = 0
        for count in counts:
            n -= count
            unreachable_count += count*n
        
        return unreachable_count