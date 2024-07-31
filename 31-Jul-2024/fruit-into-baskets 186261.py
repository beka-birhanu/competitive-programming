# Problem: fruit-into-baskets - https://leetcode.com/problems/fruit-into-baskets/

class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        in_bskt1 = [-1,-1,0]
        in_bskt2 = [-1,-1,0]

        i = 0
        ans = 0
        for j in range(len(fruits)):
            if fruits[j] == in_bskt1[0] or in_bskt1[0] == -1:
                    in_bskt1[0] = fruits[j]
                    in_bskt1[1] = j
                    in_bskt1[2] += 1

            elif fruits[j] == in_bskt2[0] or in_bskt2[0] == -1:
                    in_bskt2[0] = fruits[j]
                    in_bskt2[1] = j
                    in_bskt2[2] += 1

            else:
                while in_bskt1[2] and in_bskt2[2]:
                     
                    if fruits[i] == in_bskt1[0]:
                        in_bskt1[2] -= 1
                
                    else:
                        in_bskt2[2] -= 1

                    i += 1
                if 0 == in_bskt1[2]:
                    in_bskt1 = [fruits[j],j,1]
            
                else:
                    in_bskt2 =  [fruits[j],j,1]

            ans = max(ans,in_bskt1[2]+in_bskt2[2])

        return ans
