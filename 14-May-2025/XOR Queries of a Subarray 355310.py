# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        ans =[]
        pr =[0]
        for i in range(n):
            pr.append(arr[i]^pr[-1])
        for i,j in queries:
            ans.append(pr[i]^pr[j+1])
        return ans
        