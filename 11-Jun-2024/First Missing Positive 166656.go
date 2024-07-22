# Problem: First Missing Positive - https://leetcode.com/problems/first-missing-positive/description/

public class Solution {
    public int FirstMissingPositive(int[] nums) {
        void Swap(int i, int j, int[] arr){
            int tempo = arr[i];

            arr[i] = arr[j];
            arr[j] = tempo;
        }

        int N = nums.Length;
        int i = 0;
        while(i < N){
            if(i != nums[i]-1 && 0 <= nums[i]-1  && nums[i]-1 < N){
                if(nums[nums[i]-1] != nums[i]){
                    Swap(i, nums[i]-1, nums);
                    continue;
                }
            }

            i++;
        }
        for(int j = 0; j < N; j++){
            if(j != nums[j]-1){
                return j+1;
            }
        }

        return N+1;
    }
}