# Problem: Minimum Size Subarray in Infinite Array - https://leetcode.com/problems/minimum-size-subarray-in-infinite-array/

class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        curr_size = (target//total_sum)*len(nums)
        target %= total_sum

        left = 0
        min_size = curr_size if target == 0 else inf
        nums += nums
        for right in range(len(nums)):            
            target -= nums[right]
            curr_size += 1
            
            while target < 0:
                target += nums[left]
                left += 1
                curr_size -= 1

            if target == 0:
                min_size = min(min_size, curr_size)
        
        return min_size if min_size < inf else -1