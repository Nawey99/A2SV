# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = []
        for i in range(1,n+1):
            arr.append(i)
        count = 1 
        l = 0
        while len(arr) >1:
            if l >= len(arr):
                l = 0
            if count % k == 0:
                arr.pop(l)
                l-=1
            count +=1
            l+=1
        return arr [0]