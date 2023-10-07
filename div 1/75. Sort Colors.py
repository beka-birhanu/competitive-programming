# Rumtime 43ms and Memory 13.7Mb
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
#Runtime 43ms and Memory 16.7Mb
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0,0,0]
        for i in nums:
            count[i] += 1
        i = 0
        for idx, val in enumerate(count):
            while val:
                nums[i] = idx
                val -= 1
                i += 1 

    
