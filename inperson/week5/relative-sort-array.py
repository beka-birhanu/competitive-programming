class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        reference = {num:idx for idx,num in enumerate(arr2)}
        def compare(num):
            return num+len(reference) if num not in reference else reference[num]
        
        arr1.sort(key = compare)
        return arr1