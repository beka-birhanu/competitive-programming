def insertionSort1(n, arr):
    # Write your code here
    num = arr[n-1]
    for j in range(1,n+1):
        i = (n-1)-j
        if arr[i] > num and i >=0:
            arr.remove(arr[i+1])
            arr.insert(i+1,arr[i])
            x =''
            for i in arr:
                x += str(i) + ' '
            print(x)
        else:
            arr.remove(arr[i+1])
            arr.insert(i+1,num)
            x =''
            for i in arr:
                x += str(i) + ' '
            print(x)
            return
 
