class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0

        is_negative = num < 0

        if not is_negative:
            num = list(str(num))
            num.sort()
        else:
            num = list(str(-num))
            num.sort(reverse=True)
        if num[0] == "0":
            for i in range(len(num)):
                if num[i] != "0":
                    num[i], num[0] = num[0], num[i]
                    break

        return -int("".join(num)) if is_negative else int("".join(num))