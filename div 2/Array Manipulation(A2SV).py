def arrayManipulation(arr, queries):
    # Write your code here
    arr = [0]*(n+2)
    for start,end,k in queries:
        arr[start] +=k
        arr[end+1] -= k
        
    ans =  0
    sum_ = 0
    for  i in range (len(arr)):
        sum_  += arr[i]
        ans = max(ans,sum_)
        
    return ans
