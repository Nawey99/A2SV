# Problem: Number of Recent Calls - https://leetcode.com/problems/number-of-recent-calls/

class RecentCounter:

    def __init__(self):
        self.que = deque()
        

    def ping(self, t: int) -> int:
        self.que.append(t)
        while self.que[0]<t-3000:
            self.que.popleft()
        return len(self.que)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)