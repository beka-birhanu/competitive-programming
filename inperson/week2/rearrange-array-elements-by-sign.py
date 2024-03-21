class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:      

        ans = [0]*len(nums)
        pos_idx = 0
        neg_idx = 1

        for i in range(len(ans)):
            if nums[i] > 0:
                ans[pos_idx] = nums[i]
                pos_idx += 2
            else:

                ans[neg_idx] = nums[i]
                neg_idx += 2

        return ans
        