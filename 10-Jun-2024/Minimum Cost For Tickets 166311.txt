# Problem: Minimum Cost For Tickets - https://leetcode.com/problems/minimum-cost-for-tickets/

public class Solution {
    public int MincostTickets(int[] days, int[] costs) {
        int N = days.Length;
        int[] dp = new int[N];

        for(int i = N-1; i >= 0; i--){
            int minCost = int.MaxValue;
            int j = 0;

            foreach(int passDays in new int[]{1, 7, 30}){
                int freeFinishDay = passDays + days[i];
                int idx = Array.BinarySearch(days, freeFinishDay);
                int cost = costs[j];

                if (idx < 0) {
                    idx = ~idx;
                }

                if(idx < N){
                    cost += dp[idx];
                }

                minCost = int.Min(minCost, cost);
                j++;
            }
            dp[i] = minCost;
        }
        return dp[0];
    }
}