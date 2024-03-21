class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        in_bskt1 = (-1,-1)
        in_bskt2 = (-1,-1)

        i = 0
        ans = 0
        for j,f_type in enumerate(fruits):

            if f_type == in_bskt1[0] or in_bskt1[0] == -1:
                    in_bskt1 = (f_type,j)

            elif f_type == in_bskt2[0] or in_bskt2[0] == -1:
                    in_bskt2 = (f_type,j)

            else:
                    if  in_bskt1[1] < in_bskt2[1]:
                        i = in_bskt1[1] + 1
                        in_bskt1 = (f_type, j)
        
                    else:
                        i = in_bskt2[1] + 1
                        in_bskt2 =  (f_type, j)

            ans = max(ans,j-i+1)

        return ans
