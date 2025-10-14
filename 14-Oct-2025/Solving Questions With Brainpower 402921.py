# Problem: Solving Questions With Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        memo = {}
        
        def dp(idx):
            if idx>=n:
                return 0
            if idx not in memo:
                memo[idx] = max(questions[idx][0]+dp(idx+questions[idx][1]+1),dp(idx+1))
            return memo[idx]
        return dp(0)