class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        pref = 0
        patch_count = 0
        i = 0
        num = 0
        while num <= n:
            while i < len(nums) and num >= nums[i]:
                pref += nums[i]
                i += 1

            if pref < num:
                pref += num
                patch_count += 1

            if pref >= n:
                break
            num = pref + 1
        return patch_count