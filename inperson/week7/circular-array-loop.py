class Solution:
    def circularArrayLoop(self, A: List[int]) -> bool:
        def next_of(i):
            return (i + A[i]) % n

        n = len(A)

        for i in range(n):
            if A[i] == 0: continue

            fast = slow = i
    
            while A[fast] * A[next_of(fast)] > 0 and \
                  A[next_of(fast)] * A[next_of(next_of(fast))] > 0:
                fast = next_of(next_of(fast))
                slow = next_of(slow)
                if slow == fast:
                    if slow == next_of(slow):
                        break 
                    return True
            
            slow = i
            while slow * A[next_of(slow)] > 0:
                next_slow = next_of(slow) 
                A[slow] = 0 
                slow = next_slow
            
        return False

