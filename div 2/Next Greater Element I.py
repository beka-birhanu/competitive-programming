class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for Int in nums1:
            idx = nums2.index(Int)
            a = -1
            for n in nums2[idx+1:]:
                if n > Int:
                    a = n
                    break
            ans.append(a)
        return ans
