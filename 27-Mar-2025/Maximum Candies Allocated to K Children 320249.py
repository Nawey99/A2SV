# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def checker(x):
            count = 0
            for i in candies:
                count += i//x
            return count>=k
        low = 0
        res = 0
        high = max(candies) + 1
        while low+1 < high:
            mid = (low+high)//2
            if checker(mid):
                low = mid
            else:
                high = mid
        return low 