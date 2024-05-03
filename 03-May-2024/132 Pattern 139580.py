# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False 

        stack = deque()
        max_element = float('-inf') 

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < max_element:
                return True     
            
            while stack and stack[0] < nums[i]:
                max_element = stack.popleft() 
            
            stack.appendleft(nums[i]) 

        return False