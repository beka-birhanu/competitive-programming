# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/

public class Solution {
    public int PivotIndex(int[] nums) {
        int a=nums.Sum(),b=0;
        for(int i=0;i<nums.Length;i++){
            a-=nums[i];
            if(a==b){
            return i;
            }
            b+=nums[i];
        }
        return -1;
    }
}