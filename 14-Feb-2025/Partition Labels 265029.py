# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = defaultdict(int)
        Max = 0
        res = []
        n = len(s)
        for i in range(n):
            last[s[i]] = i
        for i in range(len(s)):
            Max = max(Max,last[s[i]])
            if Max == i:
                res.append(Max+1)
        for i in range(len(res)-1,0,-1):
            res [i] -= res[i-1]
        return res