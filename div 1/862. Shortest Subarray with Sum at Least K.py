class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        mq, ans = deque(), float('inf')
        ps = [0]
        for Int in nums:
            ps.append(ps[-1] + Int)
        for idx, s in enumerate(ps):
            # if the prefix sum of the current index has decreased 
            # it could not be the answer remove all before it which are less than 
            while mq and ps[mq[-1]] >= s:
                mq.pop()
                
            mq.append(idx)
            while mq and s - ps[mq[0]] >= k:
                ans = min(ans, idx - mq.popleft())
        return ans if ans != float('inf') else -1

