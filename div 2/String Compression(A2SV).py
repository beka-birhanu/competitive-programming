class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        j = 0

        while j < len(chars):
            char = chars[j]
            count = 0

            while j < len(chars) and char == chars[j]:
                j += 1
                count += 1

            chars[i] = char
            i += 1
            if count > 1:
                for digit in str(count):
                    chars[i] = digit
                    i += 1
        return i
