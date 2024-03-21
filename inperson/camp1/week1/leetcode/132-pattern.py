class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        st = []
        min_sofar = inf
        for num in nums:
            while st and st[-1][0] <= num:
                st.pop()
                
            if st:
                if st[-1][1] < num:
                    return True
            
            st.append((num,min_sofar)) 
            min_sofar = min(num, min_sofar)
            
        return False
            