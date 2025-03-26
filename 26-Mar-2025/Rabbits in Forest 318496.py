# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        ans = 0
        for key,value in count.items():
            temp = ceil(value/(key+1)) * (key+1)
            ans +=temp
        return ans