# Problem: Find Xor-Beauty of Array - https://leetcode.com/problems/find-xor-beauty-of-array/

public class Solution {
    public int XorBeauty(int[] nums) {
        int xor = 0;
        foreach(int val in nums){
            xor = xor ^ val;
        }
        return xor;
    }
}