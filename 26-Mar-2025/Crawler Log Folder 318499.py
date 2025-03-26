# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = []
        for i in logs:
            if i == '../':
                if ans: ans.pop()
            elif i == './':
                continue
            else:
                ans.append(i)
        print(ans)
        return len(ans)
