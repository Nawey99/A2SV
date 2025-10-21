# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/description/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        arr = [float('inf')] * n
        arr[k-1] = 0
        dic = defaultdict(list)
        for From,To,W in times:
            dic[From].append((W,To))
        que = deque()
        que.append(k)
        visited = set()
        while que:
            for i in range(len(que)):
                From = que.popleft()
                for W,To in dic[From]:
                    if arr[To-1] >arr[From-1]+W: 
                        arr[To-1] = arr[From-1]+W
                        que.append(To)
        ans = max(arr)
        return -1 if ans == float('inf') else ans