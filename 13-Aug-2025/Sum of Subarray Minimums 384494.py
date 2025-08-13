# Problem: Sum of Subarray Minimums - https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        dic_max=defaultdict(lambda: 1)
        dic_min = defaultdict(lambda: 1)
        min_stack=[]
        max_stack=[]
        n = len(arr)
        MOD = ((10**9) + 7)
        ans = 0
        for i in range(n):
            while min_stack and arr[min_stack[-1]] >= arr[i]:
                x=min_stack.pop()
                dic_min[i] += dic_min[x]
            min_stack.append(i)
        for i in range(n-1,-1,-1):
            while max_stack and arr[max_stack[-1]]>arr[i]:
                x = max_stack.pop()
                dic_max[i] += dic_max[x]
            max_stack.append(i)
        for i in range(n):
            ans += arr[i]*dic_min[i]*dic_max[i]
        return ans % MOD

