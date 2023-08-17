class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lowwerBound(lst,r,l, trgt):
            while l <= r:
                mid = (l+r)//2
                if lst[mid] == trgt:
                    r = mid - 1
                    if mid > 0 and  lst[mid-1] != trgt:
                        return mid
                elif lst[mid] > trgt:
                    r = mid - 1
                else:
                    l = mid + 1
            return l

        def upperBound(lst,r,l, trgt):
            while l <= r:
                mid = (l+r)//2
                if lst[mid] == trgt:
                    l = mid + 1
                    if mid < len(lst)-1 and lst[mid+1] != trgt:
                        return mid
                elif lst[mid] > trgt:
                    r = mid - 1
                else:
                    l = mid + 1
            return r

        l,r = 0,len(nums)-1

        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                l=r=mid
                if mid < len(nums)-1 and nums[mid+1] ==target:
                    r = upperBound(nums,len(nums)-1,mid+1,target)
                if mid > 0 and  nums[mid-1] == target:
                    l = lowwerBound(nums,mid-1,0,target)
                return [l,r]
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return [-1,-1]
