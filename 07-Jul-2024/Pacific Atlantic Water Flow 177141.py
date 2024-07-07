# Problem: Pacific Atlantic Water Flow - https://leetcode.com/problems/pacific-atlantic-water-flow

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def in_bound(row, col, row_bound, col_bound):
            return 0 <= row < row_bound and 0 <= col < col_bound
        
        def mark(queue, dp):
            while queue:
                cur_row, cur_col = queue.popleft()
                cur_height = heights[cur_row][cur_col]

                for dr, dc in DIRECTIONS:
                    nbr_row, nbr_col = cur_row+dr, cur_col + dc
                    if not in_bound(nbr_row, nbr_col, row, col):
                        continue

                    marked = dp[nbr_row][nbr_col]
                    is_higher = heights[nbr_row][nbr_col] >= cur_height

                    if not marked and is_higher:
                        dp[nbr_row][nbr_col] = True
                        queue.append((nbr_row, nbr_col))

        row = len(heights)
        col = len(heights[0])
        atlant_dp = [[False for i in range(col)] for j in range(row)]
        pacific_dp = [[False for i in range(col)] for j in range(row)]

        atlant_queue = deque()
        pacific_queue = deque()
        for i in range(col):
            atlant_dp[0][i] = True
            atlant_queue.append((0, i))

            pacific_dp[-1][i] = True
            pacific_queue.append((row-1, i))
        
        for i in range(row):
            atlant_dp[i][0] = True
            atlant_queue.append((i, 0))

            pacific_dp[i][-1] = True
            pacific_queue.append((i, col-1))          

        mark(atlant_queue, atlant_dp)
        mark(pacific_queue, pacific_dp)

        result = []

        for i in range(row):
            for j in range(col):
                if pacific_dp[i][j] and atlant_dp[i][j]:
                    result.append([i, j])
    
        return result 
                    
