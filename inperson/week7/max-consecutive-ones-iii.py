class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros = deque()
        ans = 0
        i = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                zeros.append(j)
                if len(zeros) > k:
                    i = zeros.popleft() + 1
            ans = max(ans, j-i+1)
        return ans

       