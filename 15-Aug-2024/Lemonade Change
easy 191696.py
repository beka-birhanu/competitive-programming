# Problem: Lemonade Change
easy - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill_in_hand = Counter()
        for bill in bills:
            bill_in_hand[bill] += 1

            if bill == 20 and bill_in_hand[10] > 0:
                bill_in_hand[10] -= 1
                bill -= 10

            bill_in_hand[5] -= (bill//5) -1

            if bill_in_hand[5] < 0:
                return False

        return True              
