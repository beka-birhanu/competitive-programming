class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_num = ""
        for i in range(len(num) - 2):
            current_num = ""
            if num[i] == num[i + 1] == num[i + 2]:
                max_num = max(max_num, num[i : i + 3])
        
        return max_num