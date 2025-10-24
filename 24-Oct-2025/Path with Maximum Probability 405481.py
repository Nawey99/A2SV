# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        
        arr = [float('-inf')] * n
        arr[start_node] = -1
        dic = defaultdict(list)
        for i in range(len(edges)):
            From,To = edges[i]
            W = succProb[i]
            dic[From].append((W,To))
            dic[To].append((W,From))
        que = []
        heappush(que,(-1,start_node))
        visited = set()
        while que:
            val, temp = heappop(que)
            print(val,temp)
            # if temp == end_node:
            #     return -val
            if temp not in visited:
                for W,child in dic[temp]:
                    # if child not in visited:
                        arr[child] = max(arr[child],-val*W)
                        heappush(que,(-arr[child],child))
                visited.add(temp)
        return arr[end_node] if arr[end_node] != float('-inf') else 0
 
