# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def inbound(x,y):
            return -1<x<n and -1<y <m
        def dfs(x,y):
            if not inbound(x,y):
                return 0
            if grid[x][y] == 0:
                return 0
            grid[x][y] = 0
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            ans = 1
            for i,j in directions:
                row = x+i
                col = y+j
                ans += dfs(row,col)
            return ans
        Max = 0
        n,m = len(grid),len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    Max = max(Max,dfs(i,j))
        return Max