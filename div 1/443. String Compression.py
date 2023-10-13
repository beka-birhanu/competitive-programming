# Runtime 67ms and Memory 16Mb
class Solution:
    def compress(self, chars: List[str]) -> int:
        i, j = 0, 0
        length = 0
        while i < len(chars):
            while j < len(chars) and chars[i] == chars[j]:
                j += 1
            chars[length] = chars[i]
            if j-i > 1:
                for digit in str(j-i):
                    length += 1
                    chars[length] = digit
            length += 1
            i = j
        return length 
