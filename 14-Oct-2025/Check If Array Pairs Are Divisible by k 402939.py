# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        x = [0] * k
        for i in range(len(arr)):
            x[arr[i]%k] +=1
        if  k%2 ==0 and (x[k//2]) %2 ==1:
            return False
        for i in range(1,k):
            if x[i] != x[k-i]:
                return False
        return True

