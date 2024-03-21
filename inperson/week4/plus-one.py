class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = len(digits)-1
        while carry and i > -1:
            digits[i], carry = (digits[i] + carry)%10, (digits[i] + carry)//10
            i -= 1
        if carry:
            return [1]+digits
        return digits