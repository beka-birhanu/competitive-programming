# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rowMap, colMap = {}, {}
        n = len(stones)
        rank = [1 for _ in range(n)]
        par = [i for i in range(n)]

        def find(node):
            if par[node] == node:
                return node
            par[node] = find(par[par[node]])
            return par[node]
        
        def union(node1, node2):
            par1, par2 = find(node1), find(node2)
            if par1 == par2:
                return
            
            if rank[par1] > rank[par2]:
                par[par2] = par1
            elif rank[par2] > rank[par1]:
                par[par1] = par2
            else:
                par[par2] = par1
                rank[par1] += rank[par2]

        for idx, (r, c) in enumerate(stones):
            if r in rowMap:
                # Row already seen before meaning, there is
                # a stone in that row that was previously seen
                union(idx, rowMap[r])
            else:
                # There are no stones in that row
                # Add the row to the rowMap
                rowMap[r] = idx
            
            if c in colMap:
                # Col already seen before meaning, there is
                # a stone in that col that was previously seen
                union(idx, colMap[c])
            else:
                # There are no stones in that col
                # Add the row to the colMap
                colMap[c] = idx
 
        for i in range(n):
            find(i)
        
        return n - len(set(par))
        