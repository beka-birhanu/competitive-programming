# Problem: Minimum Cost For Tickets - https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @cache
        def helper(i):
            if i >= len(days):
                return 0

            day = days[i]

            idx_after_one_pass = bisect.bisect_left(days, day+1)
            one_pass = helper(idx_after_one_pass) + costs[0]

            idx_after_week_pass = bisect.bisect_left(days, day+7)
            week_pass = helper(idx_after_week_pass) + costs[1]
        
            idx_after_month_pass = bisect.bisect_left(days, day+30)
            month_pass = helper(idx_after_month_pass) + costs[2]

            return min(one_pass, week_pass, month_pass)
        
        return helper(0)

            