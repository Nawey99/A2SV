# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r =len(height)-1
        Max = 0
        while l<r:
            k = min(height[l],height[r]) * (r-l)
            Max = max(Max, k)
            if height[l] > height[r]:
                r -=1
            else: l+=1
        return Max