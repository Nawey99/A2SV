# Problem: Heaters  - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        def bfs(i):
            n,m = len(houses),len(heaters)
            h_idx,he_idx =0,0
            while h_idx < n:
                if he_idx >=m:
                    return False
                low = heaters[he_idx] - i
                high = heaters[he_idx] + i
                if houses[h_idx] < low:
                    return False
                if houses[h_idx] > high:
                    he_idx +=1
                else:
                    h_idx +=1
            return True
        heaters.sort()
        houses.sort()
        low =0
        high = 10 ** 9
        ans = -1
        while low < high:
            mid = (low + high ) //2
            if bfs(mid):
                ans = mid
                high = mid
            else:
                low = mid+1
        return ans