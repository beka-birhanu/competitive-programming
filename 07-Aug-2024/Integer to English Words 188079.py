# Problem: Integer to English Words - https://leetcode.com/problems/integer-to-english-words/

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        
        map_ones = {
            1: 'One', 2: 'Two', 3: 'Three',
            4: 'Four', 5: 'Five', 6: 'Six',
            7: 'Seven', 8: 'Eight', 9: 'Nine',
        }
        map_from_10_to19 = {
            10: 'Ten', 11: 'Eleven', 12: 'Twelve',13: 'Thirteen',
            14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen',
            17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen',
        }
        map_tens = {
            20: 'Twenty', 30: 'Thirty', 40: 'Forty',50: 'Fifty',
            60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety',
        }

        def get_part(n):
            result = []
            hundreds = n // 100
            if hundreds:
                result.append(map_ones[hundreds])
                result.append('Hundred')
            n %= 100
            if n == 0:
                pass
            elif n < 10:
                result.append(map_ones[n])
            elif n < 20:
                result.append(map_from_10_to19[n])
            else:
                tens = n // 10
                ones = n % 10
                result.append(map_tens[10 * tens])
                if ones:
                    result.append(map_ones[ones])            
            return result

        billions = num // 1_000_000_000
        num %= 1_000_000_000
        millions = num // 1_000_000
        num %= 1_000_000 
        thousands = num // 1_000
        ones = num % 1000

        result = []
        if billions != 0:
            result.extend(get_part(billions))
            result.append('Billion')
        if millions != 0:
            result.extend(get_part(millions))
            result.append('Million')
        if thousands != 0:
            result.extend(get_part(thousands))
            result.append('Thousand')
        if ones != 0:
            result.extend(get_part(ones))
        
        return ' '.join(result)