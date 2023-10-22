class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        d={0:[0,1]}
        s=0
        ans=0
        for i in range(len(arr)):
            s^=arr[i]
            if(s in d):
                j=d[s]
                ans+=(i*j[1])-j[0]
                d[s][0]+=i+1
                d[s][1]+=1
            else:
                d[s]=[i+1,1]
                
        return ans
