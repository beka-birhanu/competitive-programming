# Problem: Maximum Performance of a Team - https://leetcode.com/problems/maximum-performance-of-a-team/

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        MOD = pow(10, 9) + 7
        efficiency_and_speed = sorted(zip(efficiency, speed), reverse = True)

        k_max_speed = []
        total_speed = 0
        max_performance = 0

        for eff, speed in efficiency_and_speed:
            heapq.heappush(k_max_speed, speed)
            total_speed += speed

            if len(k_max_speed) > k:
                total_speed -= heapq.heappop(k_max_speed)

            curr_performance = total_speed * eff
            max_performance = max(curr_performance, max_performance)
        
        return max_performance % MOD
