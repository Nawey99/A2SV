# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def checker(x):
            temp = 0
            for i in ranks:
                temp+=(floor(sqrt(x/i)))
            return temp
        low = 1
        high = max(ranks) * cars * cars
        while low <=high:
            mid = (high+low)//2
            if checker(mid) >= cars:
                high = mid-1
            else:
                low = mid+1
        return low