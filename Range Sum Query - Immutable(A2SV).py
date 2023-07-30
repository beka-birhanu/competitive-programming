class NumArray:

    def __init__(self, nums: List[int]):
        pref_sum = [0]*len(nums)
        pref_sum[0] = nums[0]
        for i in range(1,len(nums)):
            pref_sum[i] = nums[i] + pref_sum[i-1]
        self.pref_sum = pref_sum

    def sumRange(self, left: int, right: int) -> int:

        return self.pref_sum[right]-(self.pref_sum[left-1]) if left else self.pref_sum[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
