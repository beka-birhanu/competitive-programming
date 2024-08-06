# Problem: Maximum Gap - https://leetcode.com/problems/maximum-gap/

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        
        if len(nums) < 2:
            return 0

        min_val = min(nums)
        max_val = max(nums)
        
        bucket_size = max(1, (max_val - min_val) // (len(nums) - 1))
        num_buckets = (max_val - min_val) // bucket_size + 1
        
        buckets = [None] * num_buckets
        
        for num in nums:
            bucket_index = (num - min_val) // bucket_size
            if not buckets[bucket_index]:
                buckets[bucket_index] = [num,num]
            else:
                buckets[bucket_index][0] = min(buckets[bucket_index][0], num)
                buckets[bucket_index][1] = max(buckets[bucket_index][1], num)
        
        max_gap = 0
        prev_max = min_val
        for bucket in buckets:
            if bucket:
                max_gap = max(max_gap, bucket[0] - prev_max)
                prev_max = bucket[1]
        
        return max_gap