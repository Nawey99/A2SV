# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowI: int) -> List[int]:
        if rowI == 0:
            return [1]
        if rowI == 1:
            return [1,1]
        prev = self.getRow(rowI-1)
        res = [1]
        n = len(prev)
        for i in range(1,n):
            res.append(prev[i-1]+prev[i])
        res.append(1)
        return res