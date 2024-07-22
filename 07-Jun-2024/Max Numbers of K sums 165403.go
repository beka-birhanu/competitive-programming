# Problem: Max Numbers of K sums - https://leetcode.com/problems/max-number-of-k-sum-pairs

public class Solution {
    public int MaxOperations(int[] nums, int k) {
        Array.Sort(nums);
        int ops = 0;
        int i = 0;
        int j = nums.Length-1;

        while(i < j){
            int sum = nums[i] + nums[j];
            if (sum == k){
                ops++;
                i++;
                j--;
            }else if (sum < k){
                i++;
            }else{
                j--;
            }
        }

        return ops;
    }
}