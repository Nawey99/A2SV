# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        logs = path.split('/')
        ans = []
        for i in logs:
            if i == '..':
                if ans: ans.pop()
            elif i == '.' or not i:
                continue
            else:
                ans.append(i)
        return '/'+'/'.join(ans)