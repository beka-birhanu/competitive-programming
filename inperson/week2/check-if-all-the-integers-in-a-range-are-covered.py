class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        """
        this solution is aproched in prefix-sum
        time = O(1)
        space = O(1)
        """
        to_check = [0]*52
        for st,ed in ranges:
            to_check[st] += 1
            to_check[ed+1] -= 1
        
        for i in range(1,51):
            to_check[i] += to_check[i-1] 
        p = 0
        for i in to_check[left:right+1]:
            if i == 0:
                return False
        return True
