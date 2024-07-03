# Problem: Minimum Difference Between Largest and Smallest Value in 3 Moves - https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

public class Solution {
    public int MinDifference(int[] nums) {
        int N = nums.Length;
        if (N <= 4) {
            return 0;
        }

        Array.Sort(nums);

        int diff1 = nums[N-1] - nums[3];
        int diff2 = nums[N-2] - nums[2];
        int diff3 = nums[N-3] - nums[1];
        int diff4 = nums[N-4] - nums[0];

        return Math.Min(Math.Min(diff1, diff2), Math.Min(diff3, diff4));
    }
}
