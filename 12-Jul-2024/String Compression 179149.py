# Problem: String Compression - https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        j = 0
        while j < len(chars):
            char = chars[j]
            start = j
            while j < len(chars) and char == chars[j]:
                j += 1
            chars[i] = char
            i += 1
            if j - start > 1:
                for digit in str(j - start):
                    chars[i] = digit
                    i += 1
        return i