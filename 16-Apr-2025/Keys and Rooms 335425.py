# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        que = deque()
        n = len(rooms)
        que.append(0)
        visited = [0]*n
        while que:
            _n = len(que)
            for i in range(_n):
                curr = que.popleft()
                visited[curr] = 1
                for j in rooms[curr]:
                    if visited[j] != 1:
                        que.append(j)
        for i in range(n):
            if visited[i] != 1:
                return False
        return True
                