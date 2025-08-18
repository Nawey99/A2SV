# Problem: Construct Smallest Number From DI String - https://leetcode.com/problems/construct-smallest-number-from-di-string/description/

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        def bct(i,s,visited):
            if len(s) == n + 1:
                ans.append(s)
                return
            if (s[-1] == '9' and pattern[i] == "I" ) or (s[-1] == '1' and pattern[i] == "D" ):
                return
            if pattern[i] == "I":
                x= int(s[-1])
                for d in range(x+1,10):
                    if d not in visited:
                        bct(i+1,s + str(d),visited | {d})
            else:
                x= int(s[-1])
                for d in range(1,x):
                    if d not in visited:
                        bct(i+1,s + str(d),visited | {d})

        ans = []
        visited = set()
        n = len(pattern)
        for i in range(1,10):
            bct(0,str(i),visited | {i})
        Min = float("inf")
        for i in ans:
            Min = min(Min, int(i))
        return str(Min)