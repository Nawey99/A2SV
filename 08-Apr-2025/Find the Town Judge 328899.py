# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        persons = [0] * n
        for x,y in trust:
            persons [x-1] -=1
            persons [y-1] +=1
        for i in range(n):
            if persons[i] == n-1:
                return i+1
        return -1
