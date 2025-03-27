# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def checker(x):
            temp = min(position)
            count = 1
            for i in position:
                if (temp + x) <= i:
                    temp = i
                    count +=1
            return count >=m
        low = 1
        high =max(position) - min(position)
        position.sort()
        while low<=high:
            mid = (high+low)//2
            if checker(mid):
                low = mid+1
            else:
                high = mid-1
        return high