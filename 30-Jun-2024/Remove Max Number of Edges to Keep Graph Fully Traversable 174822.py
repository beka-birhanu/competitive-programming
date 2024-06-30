# Problem: Remove Max Number of Edges to Keep Graph Fully Traversable - https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        def find(representative, node):
            while representative[node] != node:
                representative[node] = representative[representative[node]]
                node = representative[node]
            return node

        MINIMUM_EDGE = 2 * (n - 1)
        alice_rep = [i for i in range(n + 1)]
        bob_rep = [i for i in range(n + 1)]

        # Sort edges in reverse order to prioritize common edges (type 3)
        edges.sort(reverse=True)
        removable_count = 0
        connected_count = 0

        for edge_type, node1, node2 in edges:
            is_removable = True

            # Alice can use type 1 or type 3 edges
            if edge_type in [1, 3]:
                rep1 = find(alice_rep, node1)
                rep2 = find(alice_rep, node2)

                if rep1 != rep2:
                    is_removable = False
                    alice_rep[rep1] = rep2
                    connected_count += 1

            # Bob can use type 2 or type 3 edges
            if edge_type in [2, 3]:
                rep1 = find(bob_rep, node1)
                rep2 = find(bob_rep, node2)

                if rep1 != rep2:
                    is_removable = False
                    bob_rep[rep1] = rep2
                    connected_count += 1

            if is_removable:
                removable_count += 1

        return removable_count if connected_count == MINIMUM_EDGE else -1
