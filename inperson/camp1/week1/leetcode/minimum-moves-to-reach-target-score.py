class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves_count = 0
        while target > 1:
            if maxDoubles:
                if not target % 2:
                    target //= 2
                    maxDoubles -= 1
                else:
                    target -= 1
                    
                moves_count += 1
            
            else:
                moves_count += target-1
                break
        return moves_count 