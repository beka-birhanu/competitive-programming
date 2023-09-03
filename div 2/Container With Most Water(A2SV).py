class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_h = max(height)
        max_area = 0
        i = 0
        j = len(height) - 1
        
        while i < j:
            max_area = max(max_area,min(height[i] , height[j])* (j-i))
            if max_area >= (j-i) * max_h:
                return max_area

            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
            
                
        return max_area
