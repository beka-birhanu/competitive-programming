class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        changes = {5:0, 10:0, 20:0}

        for bill in bills:
            changes[bill] += 1

            if bill == 5:
                continue
            
            if bill == 10:
                if not changes[5]:
                    return False

                changes[5] -= 1
            
            else:
                change = 0
                if changes[10]:
                    change += 10
                    changes[10] -= 1

                if not change:
                    if changes[5] < 3:
                        return False
                    
                    changes[5] -= 3
                else:
                    if changes[5] < 1:
                        return False
                    changes[5] -= 1
        return True