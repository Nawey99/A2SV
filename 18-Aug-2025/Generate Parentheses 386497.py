# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans =[]
        stack =[]
        def bct(openN,closeN,):
            if openN == closeN ==n:
                ans.append(''.join(stack))
                return
            if openN < n:
                stack.append('(')
                bct(openN+1,closeN)
                stack.pop()
            if closeN < openN:
                stack.append(')')
                bct(openN,closeN+1)
                stack.pop()
        bct(0,0)
        return ans

            
