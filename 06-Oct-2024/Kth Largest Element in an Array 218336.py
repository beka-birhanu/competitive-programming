# Problem: Kth Largest Element in an Array - https://leetcode.com/problems/kth-largest-element-in-an-array/description/

class Solution:
    def findKthLargest(self, nums, k):
        def quick_select(nums, k):
            pivot = nums[len(nums)//2]
            left, mid, right = [], [], []

            for num in nums:
                if num > pivot: left.append(num)
                elif num < pivot: right.append(num)
                else: mid.append(num)
            
            if k <= len(left):           return quick_select(left, k)
            if k > len(left) + len(mid): return quick_select(right, k - len(left) - len(mid))
            
            return pivot
        
        return quick_select(nums, k)