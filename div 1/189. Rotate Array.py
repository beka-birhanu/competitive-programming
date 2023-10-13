# Runtime 180ms and Memory 27.8%
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rotate(i,j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1


        if k > len(nums):
            k %= len(nums)

        rotate(0,len(nums)-1)
        rotate(0,k-1)
        rotate(k,len(nums)-1)
