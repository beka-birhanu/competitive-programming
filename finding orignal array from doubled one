from collections import Counter
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        orignal = []
        changed.sort()
        counter = Counter(changed)
        if counter[0] % 2 != 0:
            return []
        elif len(changed) % 2 != 0:
            return []
        elif changed[-1] == 0:
            return changed[:len(changed) // 2]
        elif changed[-1] == changed[0]:
            return[]
        else:
            for Int in changed:
                if Int == 0 and counter[0]>=2:
                    counter[0] -= 2
                    orignal.append(0)
                else:
                    if counter[Int] > 0 and counter[Int*2] > 0:
                        counter[Int] -= 1
                        counter[Int * 2] -= 1
                        orignal.append(Int)

            if len(orignal) == len(changed)//2:
                return orignal
            else:
                return []
