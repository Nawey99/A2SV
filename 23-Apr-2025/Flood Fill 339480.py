# Problem: Flood Fill - https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n = len(image)
        m = len(image[0])
        dir = [(1,0),(-1,0),(0,1),(0,-1)]
        init_color = image[sr][sc]
        if init_color == color:
            return image
        que= deque()
        que.append((sr,sc))
        image[sr][sc] = color
        while que:
            row, col = que.popleft()
            for dx, dy in dir:
                new_row = row + dx
                new_col = col + dy
                if 0 <= new_row < n and 0 <= new_col < m and image[new_row][new_col] == init_color:
                    que.append((new_row, new_col))
                    image[new_row][new_col] = color
        return image