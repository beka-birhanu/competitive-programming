class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        mq, mini = deque(), float('inf')
        comu_sum = [0]
        for Int in nums:
            comu_sum.append(comu_sum[-1] + Int)
        for idx, s in enumerate(comu_sum):
            # since nums have negative number create a monotonique deque of it
            while mq and comu_sum[mq[-1]] >= s:
                mq.pop()
            mq.append(idx)
            # if the sum of the window is greater than the target shrink it from the left
            while mq and s - comu_sum[mq[0]] >= k:
                mini = min(mini, idx - mq.popleft())
        return mini if mini != float('inf') else -1
