class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        nums = Counter(nums)
        for n in nums.values():
            ans += n*(n-1)//2
            
        return ans