# Problem: Subarrays with K Different Integers - https://leetcode.com/problems/subarrays-with-k-different-integers/

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        current_count = defaultdict(int)
        subary_count = 0
        far_left = 0
        near_left = 0


        for right in range(len(nums)):
            current_count[nums[right]] += 1

            while len(current_count) > k:
                current_count[nums[near_left]] -= 1

                if current_count[nums[near_left]] == 0:
                    del current_count[nums[near_left]]

                near_left += 1
                far_left = near_left

            while current_count[nums[near_left]] > 1:
                current_count[nums[near_left]] -= 1

                if current_count[nums[near_left]] == 0:
                    del current_count[nums[near_left]]

                near_left += 1
            
            if len(current_count) == k:
                subary_count += near_left - far_left + 1
        
        return subary_count
        