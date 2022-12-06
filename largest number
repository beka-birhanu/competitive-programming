class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_num = list(map(str,nums))
        largest_num =''
        while len(str_num) > 0:
            for i in str_num :
                digit = i
                for j in str_num:
                    if digit+j < j+digit:
                        digit = j
                str_num.remove(digit)
                largest_num += digit
        return str(int(largest_num))
