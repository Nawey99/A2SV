# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        in_list = defaultdict(int)
        ans = 0
        count =0
        for i,j in edges:
            in_list[j] +=1
        for i in range(n):
            if in_list[i] == 0:
                count +=1
                ans =i
            if count >1:
                return -1
        return ans