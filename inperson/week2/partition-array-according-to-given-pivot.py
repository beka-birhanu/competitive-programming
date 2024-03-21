class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        """ 
        -the key to this problem is to understand the dutch flag partitioning algorithm
        -then with little variation we can make it stable
        -the variation is to use auxilary space
        -the first iteration for dividing the array into two segments i.e smaller,and not smaller
        -the second iteration for separating the not smaller into two i.e eqaual and not equal
        """

        
        ans = [pivot] * len(nums)

        # dividing nums into smaller and not smaller
        # equal = nums[:smaller], not equal = nums[smaller:]
        smaller = 0
        for i in range(len(nums)):
            if nums[i] < pivot:
                ans[smaller] = nums[i]
                smaller += 1
        
        
        # dividing not smaller into equal and not equal
        # equal = nums[smaller:larger+1], not equal = nums[larger+1:]  
        larger = len(nums)-1

        for i in range(len(nums)-1,-1,-1):

            if nums[i] > pivot:
                ans[larger] = nums[i]
                larger -= 1

        return ans
                
        
