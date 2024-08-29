# Problem: The kth Factor of n - https://leetcode.com/problems/the-kth-factor-of-n/

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        first_half = []
        second_half = []

        div = 1
        while div**2 <= n:
            if n % div == 0:
                first_half.append(div)
                if n // div > div:
                    second_half.append(n//div)

            div += 1
        
        if k <= len(first_half):
            return first_half[k-1]
        
        elif k - len(first_half) <= len(second_half):
            return second_half[-k + len(first_half)]
        
        else:
            return -1