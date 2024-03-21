class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)

        # first prepare for the loop back next greater
        dq = deque(nums)
        for num in reversed(nums):
            while dq and dq[0] <= num:
                dq.popleft()

            dq.appendleft(num)
        
        #now that the loop back is prepared lets find the answer
        for idx in range(len(nums)-1,-1,-1):
            num = nums[idx]
            
            while dq and dq[0] <= num:
                dq.popleft()

            if dq:
                ans[idx] = dq[0]

            dq.appendleft(num)

        return ans