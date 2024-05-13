# Problem: Find Center of Star Graph - https://leetcode.com/problems/find-center-of-star-graph/

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        seen = set()
        for n1, n2 in edges:
            if n1 in seen:
                return n1

            seen.add(n1)
            if n2 in seen:
                return n2
            
            seen.add(n2)