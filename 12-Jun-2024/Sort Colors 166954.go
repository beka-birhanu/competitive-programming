# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

public class Solution {
    public void SortColors(int[] nums) {
        int redBound = 0;
        int blueBound = nums.Length-1;
        int seeker = 0;

        while (seeker <= blueBound){
            if (nums[seeker] == 1){
                seeker++;
            } else if (nums[seeker] == 0){
                nums[seeker] = nums[redBound];
                nums[redBound] = 0;
                redBound++;
                seeker++;
            }else{
                nums[seeker] = nums[blueBound];
                nums[blueBound] = 2;
                blueBound--;
            }


        }
    }
}