class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxA = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            width = right - left
            length = min(height[left] , height[right])
            maxA = max(maxA,length* width)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
                
        return maxA


# i dont know if this could work when the widht more significantly changing than the height
