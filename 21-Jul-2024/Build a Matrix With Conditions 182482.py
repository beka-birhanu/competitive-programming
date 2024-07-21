# Problem: Build a Matrix With Conditions - https://leetcode.com/problems/build-a-matrix-with-conditions/

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def calc_positions(graph, dependency):
            queue = deque()
            for i in range(1,k+1):
                if dependency[i] == 0:
                    queue.append(i)

            positions = {}  
            while queue:
                node = queue.popleft()
                positions[node] = len(positions)

                for child in graph[node]:
                    dependency[child] -= 1
                    if dependency[child] == 0:
                        queue.append(child)
            
            return positions
        
        def buildMatrix(row_positions, col_positions, k):
            matrix = [[0]*k for _ in range(k)]
            for i in range(1, k+1):
                row = row_positions[i]
                col = col_positions[i]
                matrix[row][col] = i
            
            return matrix
        
        row_graph =[[] for _ in range(k+1)]
        col_graph = [[] for _ in range(k+1)]
        row_dependency = [0]*(k+1)
        col_dependency = [0]*(k+1)

        for parent, child in rowConditions:
            row_graph[parent].append(child)
            row_dependency[child] += 1

        for parent, child in colConditions:
            col_graph[parent].append(child)
            col_dependency[child] += 1
        
        row_positions = calc_positions(row_graph, row_dependency)
        if len(row_positions) != k:
            return []

        col_positions = calc_positions(col_graph, col_dependency)
        if len(col_positions) != k:
            return []
        
        return buildMatrix(row_positions, col_positions, k)
        
