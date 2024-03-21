class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        idx_map = defaultdict(lambda :-1)
        for idx, val in enumerate(nums1):
            idx_map[val] = idx

        ans = nums1
        ans.append(0) #for all the elements that are not required. this will be popped finally
        
        dq = deque()
        for num in reversed(nums2):
            
            while dq and dq[0] <= num:
                dq.popleft()

            ans[idx_map[num]] = dq[0] if dq else -1
            dq.appendleft(num)

        ans.pop()
        return ans
            
        