# Problem: Three sum - https://leetcode.com/problems/3sum/

public class Solution {
    public IList<IList<int>> ThreeSum(int[] nums) {
        IList<IList<int>> triplets = new List<IList<int>>();
        Array.Sort(nums);

        for (int i = 0; i < nums.Length - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue; // Skip duplicate elements for i

            int target = -nums[i];
            int j = i + 1;
            int k = nums.Length - 1;

            while (j < k) {
                int sum = nums[j] + nums[k];

                if (sum == target) {
                    triplets.Add(new List<int> { nums[i], nums[j], nums[k] });

                    // Skip duplicate elements for j and k
                    while (j < k && nums[j] == nums[j + 1]) j++;
                    while (j < k && nums[k] == nums[k - 1]) k--;

                    j++;
                    k--;
                } else if (sum < target) {
                    j++;
                } else {
                    k--;
                }
            }
        }

        return triplets;
    }
}
