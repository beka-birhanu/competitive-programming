# Problem: Subsets - https://leetcode.com/problems/subsets/

public class Solution {
    public IList<IList<int>> Subsets(int[] nums) {
        List<IList<int>> powerSet = new List<IList<int>>();
        int n = nums.Length;

        for (int mask = 0; mask < 1 << n; mask++){
            List<int> subset = new List<int>();

            int j = 0;
            int tempMask = mask;
            while(tempMask > 0){
                bool useJthElement = ((tempMask & 1) == 1);
                tempMask >>= 1;
                if (useJthElement){
                    subset.Add(nums[j]);
                }
                j++;
            }
            powerSet.Add(subset);
        }
        return powerSet;
    }
}
