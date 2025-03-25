# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def checker(val):
            n = len(weights)
            Sum = 0
            count = 1
            for i in range(0,n):
                Sum +=weights[i]
                if Sum > val:
                    Sum = weights[i]
                    count +=1
                if count > days:
                    return False
            return True
        low = max(weights)
        high = sum(weights)
        while low <=high:
            mid = (low+high)//2
            if checker(mid):
                high = mid-1
            else:
                low = mid+1
        return low



