class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @lru_cache
        def get_score(i,j):

            if j - i == 0:
                return nums[i]

            return max(nums[i] - get_score(i+1,j), nums[j] - get_score(i, j-1))

        return get_score(0,len(nums)-1) >= 0