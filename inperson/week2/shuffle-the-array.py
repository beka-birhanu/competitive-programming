class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = [0]*len(nums)
        for i in range(len(nums)//2):
            ans[2*i] = nums[i]
            ans[2*i+1] = nums[i+len(nums)//2]
        return ans 