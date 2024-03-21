class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        sum_min = 0
        stk = []

        for i in range(n):
            while stk and stk[-1][0] > arr[i]:
                prev_min, prev_min_idx = stk.pop()
                start = -1
                if stk:
                    start = stk[-1][1]

                sum_min += (i - prev_min_idx)  * (prev_min_idx - start) * prev_min

            stk.append((arr[i],i))

        while stk:
            prev_min, prev_min_idx = stk.pop()
            start = -1
            if stk:
                start = stk[-1][1]

            sum_min += (n - prev_min_idx)  * (prev_min_idx - start) * prev_min

        return sum_min % (10**9 + 7)