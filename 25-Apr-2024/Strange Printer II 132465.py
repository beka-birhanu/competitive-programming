# Problem: Strange Printer II - https://leetcode.com/problems/strange-printer-ii/

class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        def check_printablity(color, printing_state, sequence_graph):

            for next_color in sequence_graph[color]:
                if printing_state[next_color]  == 1:
                    return False

                printing_state[next_color]  = 1

                if not check_printablity(next_color, printing_state, sequence_graph):
                    return False

            printing_state[color]  = 2
            
            return True

        n = len(targetGrid)
        m = len(targetGrid[0])
        row_bounds = defaultdict(lambda : [n, 0]) #min_row, max_row
        col_bounds = defaultdict(lambda : [m, 0]) #min_col, max_col

        for i in range(n):
            for j in range(m):
                color = targetGrid[i][j]
                row_bounds[color][0] = min(i, row_bounds[color][0])
                row_bounds[color][1] = max(i, row_bounds[color][1])

                col_bounds[color][0] = min(j, col_bounds[color][0])
                col_bounds[color][1] = max(j, col_bounds[color][1])
        
        # graph representing the sequence of the print procces
        sequence_graph = defaultdict(set)

        for color, row_bound in row_bounds.items():
            min_row_bound, max_row_bound = row_bound
            min_col_bound, max_col_bound = col_bounds[color]
            
            for i in range(min_row_bound, max_row_bound+1):
                for j in range(min_col_bound, max_col_bound+1):
                    if targetGrid[i][j] != color:
                        sequence_graph[color].add(targetGrid[i][j])
                        
        
        # if there is a cycle in the sequence graph the answer is false
        printing_state = defaultdict(int) # 0 means not printed 1 means it is being printed 2 means it has been printed

        for color in row_bounds:
            if printing_state[color] == 0:
                printing_state[color] = 1

                if not check_printablity(color, printing_state, sequence_graph):
                    return False

        return True
        