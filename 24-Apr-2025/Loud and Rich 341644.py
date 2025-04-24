# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        dic = defaultdict(list)
        arr = [0] *n
        for a,b in richer:
            dic[b].append(a)
            arr[a] +=1
        ans = []
        for i in range(n):
            visited = set()
            _Min = i
            que = deque()
            que.append(i)
            while que:
                _n = len(que)
                for _ in range(_n):
                    curr = que.popleft()
                    if curr not in visited:
                        visited.add(curr)
                        if quiet[curr] < quiet[_Min]:
                            _Min = curr
                        que.extend(i for i in dic[curr])
            ans.append(_Min)
        return ans