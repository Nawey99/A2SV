# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, fl: List[List[int]], sl: List[List[int]]) -> List[List[int]]:
        i,j,n1,n2=0,0,len(fl),len(sl)
        res = []
        while i<n1 and j<n2:
            first_start,first_end = fl[i]
            second_start,second_end = sl[j]

            start_interval = max(first_start,second_start)
            end_interval = min(first_end,second_end)

            if start_interval <= end_interval :
                res.append([start_interval,end_interval])
            
            if first_end < second_end:
                i+=1
            else:
                j+=1
        return res
