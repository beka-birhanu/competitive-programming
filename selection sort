class Solution: 
    def select(self, arr, i):
        # code here 
        return min(arr[i:])
    
    def selectionSort(self, arr,n):
        for i in range(n):
            min_idx = arr.index(self.select(arr,i),i)
            if arr[i] > self.select(arr,i):
                arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr
