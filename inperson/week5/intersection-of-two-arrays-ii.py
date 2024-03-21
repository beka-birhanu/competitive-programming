class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        ans = []

        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):
            while j < len(nums2) and nums1[i] > nums2[j]:
                j += 1

            while i < len(nums1) and j < len(nums2) and nums1[i] < nums2[j]:
                i += 1
            
            while j < len(nums2) and i < len(nums1) and  nums1[i] == nums2[j]:
                ans.append(nums1[i])
                i += 1
                j += 1
        return ans 
        