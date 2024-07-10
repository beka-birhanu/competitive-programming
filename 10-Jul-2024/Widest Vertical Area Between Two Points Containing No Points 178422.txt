# Problem: Widest Vertical Area Between Two Points Containing No Points - https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/

public class Solution {
    public int MaxWidthOfVerticalArea(int[][] points) {
        Array.Sort(points, (a, b) => a[0].CompareTo(b[0]));
        int maxArea = 0;

        for(int i = 1; i < points.Length; i++) {
            int curr = points[i][0];
            int prev = points[i-1][0];

            maxArea = Math.Max(maxArea, curr - prev);
        }
        return maxArea;
    }
}