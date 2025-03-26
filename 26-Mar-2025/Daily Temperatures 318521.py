# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for idx, curr in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < curr:
                prev_idx = stack.pop()
                ans[prev_idx] = idx - prev_idx
            stack.append(idx)
        return ans
