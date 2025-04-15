# Problem: Nearest Exit from Entrance in Maze - https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        que = deque()
        n = len(maze)
        m = len(maze[0])
        dir = [(1,0),(-1,0),(0,1),(0,-1)]
        que.append((entrance[0],entrance[1],0))
        maze[entrance[0]][entrance[1]] = '+'
        def inbound(i,j):
            return -1<j<m and -1<i<n
        while que:
            i,j,step = que.popleft()
            for row,col in dir:
                    r = i+row
                    c = j+col
                    if inbound(r,c) and maze[r][c] == '.':
                        if c == 0 or c ==m-1 or r == 0 or r == n-1:
                            return step+1
                        maze[r][c] = '+'
                        que.append((r,c,step+1))
        return -1