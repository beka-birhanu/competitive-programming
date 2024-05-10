# Problem: Maximize Happiness of Selected Children - https://leetcode.com/problems/maximize-happiness-of-selected-children/?envType=daily-question&envId=2024-05-09

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        total_happiness = 0
        turn = 0
        happiness_heap = [-value for value in happiness]
        heapq.heapify(happiness_heap)

        while turn < k and happiness_heap:
            curr_max_happiness = - heapq.heappop(happiness_heap) - turn

            if curr_max_happiness <= 0:
                break

            total_happiness += curr_max_happiness
            turn += 1

        return total_happiness
