# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n= len(heights)
        _levels = []
        ans = -1
        arr = [0]
        for i in range(1,n):
            arr.append(max(heights[i]-heights[i-1],0))
        print(arr)
        for value in arr:
            if value == 0:
                ans +=1
            else:
                if len(_levels)< ladders:
                    ans+=1
                    heappush(_levels,value)
                else:
                    heappush(_levels,value)
                    temp = heappop(_levels)
                    if temp <= bricks:
                        bricks -= temp
                        ans +=1
                    else:
                        break
        return ans