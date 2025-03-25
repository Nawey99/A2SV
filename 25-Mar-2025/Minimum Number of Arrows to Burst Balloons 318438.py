# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        n = len(points)
        arr = [points[0]]
        for i in range(0,n):
            if arr[-1][1] >=points[i][0]:
                arr[-1][0] = max(arr[-1][0],points[i][0])
                arr[-1][1] = min(arr[-1][1],points[i][1])
            else:
                arr.append(points[i])
        return len(arr) 
        