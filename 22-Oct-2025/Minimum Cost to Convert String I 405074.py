# Problem: Minimum Cost to Convert String I - https://leetcode.com/problems/minimum-cost-to-convert-string-i/description/?envType=problem-list-v2&envId=shortest-path

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        arr = [[float('inf')]* 26 for _ in range(26)]
        n = 26
        for i in range(n):
            arr[i][i] = 0
        for i in range(len(cost)):
            arr[ord(original[i])-97][ord(changed[i])-97] = min(arr[ord(original[i])-97][ord(changed[i])-97],cost[i])
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])
        ans = 0
        for i in range(len(target)):
            if arr[ord(source[i])-97][ord(target[i])-97] == float('inf'):
                return -1
            ans+= arr[ord(source[i])-97][ord(target[i])-97]
        return ans
                