class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        
        for x,y in ghosts:
            if abs(x-target[0])+abs(y-target[1]) <= abs(target[0])+abs(target[1]):
                return False
        return True