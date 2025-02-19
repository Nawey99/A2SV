# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], req: List[List[int]]) -> int:
        n=len(nums)
        total =0
        arr = [0] *n
        for l,r in req:
            arr[l] +=1
            if r+1 < n:
                arr[r+1] -=1
        run_sum = [arr[0]]
        for i in range(1,n):
            run_sum.append(run_sum[-1] + arr[i])
        run_sum.sort()
        nums.sort()
        for i in range(n):
            total += run_sum[i] * nums[i]
        return total % (10**9 + 7)
