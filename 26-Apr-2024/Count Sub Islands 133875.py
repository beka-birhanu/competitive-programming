# Problem: Count Sub Islands - https://leetcode.com/problems/count-sub-islands/

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def in_bound(position, bound):
            row, col = position
            row_bound, col_bound = bound

            return 0 <= row < row_bound and 0 <= col < col_bound

        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m, n = len(grid1), len(grid1[0])
        island_number = defaultdict(lambda : -1)
        islands_count = 0
        
        # collect the island muber each cell in grid1 belongs to
        for row in range(m):
            for col in range(n):
                if grid1[row][col] == 1:
                    # all the cells in this island will have island number of curr island_count
                    st = [(row, col)] #coordinate
                    while st:
                        i, j = st.pop()
                        island_number[(i, j)] = islands_count

                        for di, dj in DIRECTIONS:
                            nbr_i, nbr_j = i + di, j + dj
                            if in_bound((nbr_i, nbr_j), (m, n)) and grid1[nbr_i][nbr_j] == 1:
                                grid1[nbr_i][nbr_j] = 0
                                st.append((nbr_i, nbr_j))
                    
                    islands_count += 1
        
        sub_island_count = 0
        # check for every island in grid2
        # if all of its cells are in same island number in grid1
        for row in range(m):
            for col in range(n):
                if grid2[row][col] == 1:
                    is_subisland = True
                    curr_island_number = island_number[(row, col)]
                     # all the cells in this island must have island number of curr_island_number
                    st = [(row, col)] #coordinate
                    while st:
                        i, j = st.pop()
                        if island_number[(i, j)] == -1 or island_number[(i, j)] != curr_island_number:
                            is_subisland = False

                        for di, dj in DIRECTIONS:
                            nbr_i, nbr_j = i + di, j + dj
                            if in_bound((nbr_i, nbr_j), (m, n)) and grid2[nbr_i][nbr_j] == 1:
                                grid2[nbr_i][nbr_j] = 0
                                st.append((nbr_i, nbr_j))
                    
                    if is_subisland:
                        sub_island_count += 1
            
        return sub_island_count
