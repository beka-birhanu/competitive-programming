# Problem: Ugly Number II - https://leetcode.com/problems/ugly-number-ii/

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_numbers = [1] * n
        
        # Pointers for multiples of 2, 3, and 5
        i2, i3, i5 = 0, 0, 0
        
        for i in range(1, n):
            next_ugly = min(ugly_numbers[i2] * 2, ugly_numbers[i3] * 3, ugly_numbers[i5] * 5)
            ugly_numbers[i] = next_ugly
            
            if next_ugly == ugly_numbers[i2] * 2:
                i2 += 1
            if next_ugly == ugly_numbers[i3] * 3:
                i3 += 1
            if next_ugly == ugly_numbers[i5] * 5:
                i5 += 1
                
        return ugly_numbers[-1]
