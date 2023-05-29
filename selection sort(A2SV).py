class Solution: 
    def select(self, arr, i):
        # code here 
        min_idx = i
        for j in range(i,len(arr)):
            if arr[j]< arr[min_idx]:
                min_idx = j
        return min_idx 
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            j = self.select(arr,i)
            arr[i],arr[j] = arr[j],arr[i]
