class Solution:
    def trap(self, height: List[int]) -> int:
        mon_st = []
        total_collected = 0
        for idx,h in enumerate(height):
            offset = 0
            while mon_st and mon_st[-1][0] <= h:
                prev = mon_st.pop()
                total_collected += (prev[0]-offset) * (idx - prev[1]-1)
                offset = prev[0]

            if mon_st:
                total_collected += (h-offset) * (idx -mon_st[-1][1]-1)

            mon_st.append((h,idx))
                
        return total_collected