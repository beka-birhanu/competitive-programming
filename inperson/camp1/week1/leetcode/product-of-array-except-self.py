class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[1]*n
        pre = 1
        post = 1
        for i in range(1,n):
            pre = pre*nums[i-1]
            ans[i] *= pre
            post = post*nums[n-i]
            ans[n-i-1] *= post
            
        return ans