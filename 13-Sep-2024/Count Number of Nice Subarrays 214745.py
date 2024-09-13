# Problem: Count Number of Nice Subarrays - https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        N = len(nums)
        odd_count = 0
        far_left = 0
        near_left = 0
        nice_count = 0

        nums.append(1) # to be like a bounder for the last subarray
        for right in range(N+1):
            is_odd = nums[right] % 2 == 1
            if is_odd:
                odd_count += 1
            
            while odd_count > k:
                nice_count += right-near_left
                if nums[far_left] % 2 == 1:
                    odd_count -= 1
                far_left += 1
            
            if is_odd:
                near_left = right

        nums.pop()
        return nice_count
