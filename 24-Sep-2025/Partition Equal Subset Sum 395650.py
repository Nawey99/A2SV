# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo ={}
        def dp(idx,tk):
            if tk == total // 2:
                return True
            if idx >=len(nums) or tk  > total // 2:
                return False

            if (idx,tk) not in memo:
                # take
                take = dp(idx+1,tk+nums[idx])

                if take == True:
                    return True

                #notake
                notake = dp(idx+1,tk)
                memo[(idx,tk)] = notake or take

            return memo[(idx,tk)]
        total = sum(nums)
        if total & 1:
            return False

        return dp(0,0)