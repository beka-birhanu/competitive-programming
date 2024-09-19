# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution(object):
    def getLucky(self, s, k):
        number = ''
        for x in s:
            number += str(ord(x) - ord('a') + 1)
        k = min(k, 4)
        while k > 0:
            temp = 0
            for x in number:
                temp += int(x)  
            number = str(temp)  
            k -= 1
        return int(number) 