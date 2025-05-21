# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        last_num = float('-inf')
        stack =[]
        for i in reversed(nums):
            if i < last_num:
                return True
            while stack and stack[-1] < i :
                last_num = stack.pop()
            stack.append(i)
        return False