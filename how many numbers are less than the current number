class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        answer = []
        for num in nums:
            count = 0
            for comp in nums:
                if num > comp:
                    count += 1
            answer.append(count)
        return answer
