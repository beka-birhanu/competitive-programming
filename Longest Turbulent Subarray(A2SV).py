class Solution:
    def maxTurbulenceSize(self, arr: list[int]) -> int:
        ans = 1
        j = 0
        last_opp = 0

        for i in range(1,len(arr)):
            if arr[i-1] > arr[i]:
                if last_opp > 0:
                    j = i-1
                last_opp = 1
            elif arr[i-1] < arr[i]:
                if last_opp < 0:
                    j = i-1
                last_opp = -1
            elif arr[i-1] == arr[i]:
                j = i
                last_opp = 0

            ans = max(ans,i-j+1)

        return ans
