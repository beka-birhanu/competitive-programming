# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:        
        tree_graph = [set() for _ in range(n)] #representaion of the tree as 
        
        for a, b in edges:
            tree_graph[a].add(b)
            tree_graph[b].add(a)
        
        # Find all leaf nodes (i.e., nodes with degree 1)
        leaves = [i for i in range(n) if len(tree_graph[i]) <= 1]
        
        # Repeat until we are left with 1 or 2 nodes
        while n > 2:
            
            # Remove the current leaf nodes along with their edges
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = tree_graph[leaf].pop()
                tree_graph[neighbor].remove(leaf)
                
                # If the neighbor becomes a new leaf node, add it to the list
                if len(tree_graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            
            # Update the list of leaf nodes
            leaves = new_leaves
        
        return leaves
