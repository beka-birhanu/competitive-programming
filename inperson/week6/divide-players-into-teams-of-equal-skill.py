class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        j = len(skill)-1
        output = 0
        tt_skill = skill[j] + skill[0]
        for i in range(j//2 + 1):
            if skill[j] + skill[i] != tt_skill:
                return -1
            output += skill[j] * skill[i]
            j -= 1
        return output