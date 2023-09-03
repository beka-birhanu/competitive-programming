class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_len = 0
        left, right = 0, 0
        n = len(nums)

        decrs_q = deque() # stores index of the max at the front
        incrs_q = deque() # stores index of the min at the front

        while right < n:
            while decrs_q and nums[decrs_q[-1]] < nums[right]:
                decrs_q.pop()
            decrs_q.append(right)
            while incrs_q and nums[incrs_q[-1]] > nums[right]:
                incrs_q.pop()
            incrs_q.append(right)

            while nums[decrs_q[0]] - nums[incrs_q[0]] > limit:
                left += 1
                if incrs_q[0] < left: incrs_q.popleft()
                if decrs_q[0] < left: decrs_q.popleft()

            max_len = max(right - left + 1, max_len)

            right += 1

        return max_len
