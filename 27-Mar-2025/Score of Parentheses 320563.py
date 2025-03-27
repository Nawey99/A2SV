# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = current_depth = 0
        for i in range(len(s)):
            if s[i] == '(': 
                current_depth += 1 
            else:
                current_depth -= 1
                if s[i - 1] == '(':
                    score += pow(2, current_depth)
        return score