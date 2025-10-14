# Problem: Minimum Path Sum - https://leetcode.com/problems/minimum-path-sum/description/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def inbound(x,y):
            return -1<x<m and -1<y<n
        n,m = len(grid[0]),len(grid)
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                x,y=float('inf'),float('inf')
                if inbound(i+1,j):
                    x=grid[i+1][j]
                if inbound(i,j+1):
                    y = grid[i][j+1]
                z = min(x ,y)
                grid[i][j]+=0 if z==float('inf') else z
        return grid[0][0]