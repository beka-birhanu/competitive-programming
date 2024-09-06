# Problem: Integer to English Words - https://leetcode.com/problems/integer-to-english-words/

from collections import deque

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        
        ones_map = {
            1: 'One', 2: 'Two', 3: 'Three',
            4: 'Four', 5: 'Five', 6: 'Six',
            7: 'Seven', 8: 'Eight', 9: 'Nine',
        }
        teens_map = {
            10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen',
            14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen',
            17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen',
        }
        tens_map = {
            20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty',
            60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety',
        }

        large_number_names = ['', 'Thousand', 'Million', 'Billion']

        def convert_chunk(n):
            words = []
            if n >= 100:
                hundreds = n // 100
                words.append(ones_map[hundreds])
                words.append('Hundred')
                n %= 100
            if 10 <= n < 20:
                words.append(teens_map[n])
            else:
                if n >= 20:
                    tens = (n // 10) * 10
                    words.append(tens_map[tens])
                    n %= 10
                if n > 0:
                    words.append(ones_map[n])
            return words

        result = deque()
        large_number_index = 0

        while num > 0:
            chunk = num % 1000
            num //= 1000
            if chunk > 0:
                chunk_words = convert_chunk(chunk)
                if large_number_names[large_number_index]:
                    chunk_words.append(large_number_names[large_number_index])
                result.appendleft(" ".join(chunk_words))
            large_number_index += 1

        return ' '.join(result)
