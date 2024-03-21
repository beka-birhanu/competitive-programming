class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeros = deque()
        ans = 0
        i = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                zeros.append(j)
                if len(zeros) > 1:
                    i = zeros.popleft() + 1
            ans = max(ans, j-i)
        return ans