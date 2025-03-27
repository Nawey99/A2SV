# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        n = 0
        for i in tokens:
            if i == '+' or  i == '-'or  i == '*'or  i == '/':
                if n >=2:
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(int(eval(f'{a}{i}{b}')))
                    n-=1
            else:
                stack.append(i)
                n+=1
        return int(stack[0])
