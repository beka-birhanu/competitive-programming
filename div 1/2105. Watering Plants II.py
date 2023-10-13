# Runtime 699ms and Memory 31 mb
class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        a, b = 0, len(plants)-1
        A, B = capacityA, capacityB
        refill_cnt = 0
        while a < b:
            if A < plants[a]:
                refill_cnt += 1
                A = capacityA
            if B < plants[b]:
                refill_cnt += 1
                B = capacityB
            A -= plants[a]
            B -= plants[b]

            a += 1
            b -= 1
        return refill_cnt + 1 if max(A, B) < plants[b] and a == b else refill_cnt
