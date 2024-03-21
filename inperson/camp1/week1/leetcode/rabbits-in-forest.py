class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answers.sort()
        min_rabbit_count = 0
        left = 0
        while left < len(answers):
            right = left + 1
            while right < len(answers) and (right - left) < (answers[left]+1) and answers[right] == answers[left]:
                right += 1

            min_rabbit_count += answers[left]+1
            left = right

        return min_rabbit_count

