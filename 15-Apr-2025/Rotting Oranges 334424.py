# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        que = deque()
        n = len(grid)
        flag = 0
        for i in range(n):
            for j in range(len(grid[i])):
                if grid[i][j] ==2:
                    que.append([grid[i][j],(i,j),0])
                elif grid[i][j] ==1:
                    flag = 1
        if len(que) == 0 and flag == 1:
            return -1
        elif len(que) == 0 and flag == 0:
            return 0
        dir = [(1,0),(-1,0),(0,1),(0,-1)]
        Max = 0
        while que:
            curr = que.popleft()
            if curr[0] == 2:
                i,j = curr[1]
                for k,z in dir:
                    n_i = i+k
                    n_j = j+z
                    if -1<n_j<len(grid[i]) and -1<n_i<n:
                        if grid[n_i][n_j] ==1 :
                            step = curr[2]
                            Max = max(Max,step+1)
                            grid[n_i][n_j] = 2
                            que.append([grid[n_i][n_j],(n_i,n_j),step+1])
        for i in grid:
            for j in i: 
                if j == 1:
                    return -1
        return Max
