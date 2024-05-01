# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree = [0] * (n + 1)
        
        for edge in edges:
            indegree[edge[1]] += 1
        
        good = []
        for i in range(n):
            if indegree[i] == 0:
                good.append(i)
        
        return good[0] if len(good) == 1 else -1
