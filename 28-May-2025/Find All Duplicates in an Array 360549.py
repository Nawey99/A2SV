# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        sets = set()
        res = []
        for i in nums:
            if i in sets:
                res.append(i)
            else:
                sets.add(i)
        return (res)