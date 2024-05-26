# Problem: Minimum Number of Days to Make m Bouquets - https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def check_possiblity(bloom_days, m, k, max_wait):
            i = 0
            for j in range(len(bloom_days)):
                if bloom_days[j] > max_wait:
                    i = j + 1

                flower_taken = j-i+1
                if flower_taken == k:
                    m -= 1
                    i = j+1

                if m == 0:
                    return True

            return False

        flowers = len(bloomDay)

        if m * k >  flowers:
            return -1
        
        candidate_days = sorted(set(bloomDay))

        left = 0
        right = len(candidate_days)-1

        while left < right:
            mid = (left+right)//2
            max_wait = candidate_days[mid]

            is_possible = check_possiblity(bloomDay, m, k, max_wait)

            if is_possible:
                right = mid
            
            else:
                left = mid+1
        
        return candidate_days[right]
            

























