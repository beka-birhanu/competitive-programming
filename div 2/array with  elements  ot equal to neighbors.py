class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        def unarranged (nums):
            for i in range(1,len(nums)-1):
                if (nums[i-1] + nums[i+1]) /2 == nums[i]:
                    return True
            return False
        while unarranged (nums):
            random.shuffle(nums)
        return nums
