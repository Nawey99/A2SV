# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        def rec(l,r,turn):
            if l ==r:
                if turn == 1:
                    return -nums[r]
                else:
                    return nums[r]
            if turn ==1:
                left = -nums[l] + rec(l+1,r,0)
                right = -nums[r] + rec(l,r-1,0)
                return min(left,right)
            elif turn ==0:
                left = nums[l] +rec(l+1,r,1)
                right = nums[r] + rec(l,r-1,1)
                return max(left,right)
        return rec(0,n-1,0)>=0