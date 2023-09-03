class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        orignal = []
        changed.sort()
        if changed.count(0)%2 != 0:
            return []
        elif changed[-1] == 0 and len(changed) % 2 == 0:
            return changed[:len(changed) // 2]
        elif changed[-1] == changed[0] and len(changed) % 2 == 0:
            return[]

        elif len(changed) %2 != 0:
            return []

        else:
            for _ in range(len(changed)):

                if len(changed) == 0:
                    return orignal
                i = changed[0]
                if i % 2 != 0 and i * 2 in changed:
                    orignal.append(i)
                    changed.remove(i)
                    changed.remove((i * 2))

                elif i % 2 == 0 and i * 2 in changed:
                    orignal.append(i)
                    changed.remove(i)
                    changed.remove((i * 2))
            if len(changed) == 0:
                return orignal
            else:
                return[]


