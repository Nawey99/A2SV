# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        n = 1<<n
        ans =[]
        for i in range(n):
            _temp=[]
            temp = bin(i)
            _n = len(temp)
            for i in range(2,_n):
                if int(temp[i]) & 1:
                    _temp.append(nums[_n-i-2])
            ans.append(_temp)
            _temp =[]
        return ans