# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        if n % 2 != 0: 
            return -1
        x = sum(skill)//(n//2)
        skill.sort()
        l = 0
        r = len(skill)-1
        count = 0
        
        while l < r:
            if skill[l] + skill[r] != x:
                return -1 
            count += skill[l] * skill[r]
            l += 1
            r -= 1
        return count
