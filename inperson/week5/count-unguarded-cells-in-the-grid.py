class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        guards = set((i,j) for i,j in guards)
        walls = set((i,j) for i,j in walls)
        guarded = set()

        for pos_i,pos_j in guards:

            i, j = pos_i+1, pos_j
            while i < m and (i,j) not in guards and (i,j) not in walls :
                guarded.add((i,j))
                i += 1

            i, j = pos_i, pos_j+1
            while j < n and (i,j) not in guards and (i,j) not in walls :
                guarded.add((i,j))
                j += 1
            
            i, j = pos_i, pos_j-1
            while j >= 0 and (i,j) not in guards and (i,j) not in walls :
                guarded.add((i,j))
                j -= 1
            
            i, j = pos_i-1, pos_j
            while i >= 0 and (i,j) not in guards and (i,j) not in walls :
                guarded.add((i,j))
                i -= 1
  

        return m*n - len(guards) - len(walls) - len(guarded)