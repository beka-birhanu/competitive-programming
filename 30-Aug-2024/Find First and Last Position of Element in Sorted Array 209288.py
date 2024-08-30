# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = bisect.bisect_left(nums, target)
        end = bisect.bisect_right(nums, target)-1

        return[start, end] if start < len(nums) and nums[start] == target else [-1,-1]