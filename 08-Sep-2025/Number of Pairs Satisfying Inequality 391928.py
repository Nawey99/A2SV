# Problem: Number of Pairs Satisfying Inequality - https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        n = len(nums1)
        nums3 =[]
        for i in range(n):
            nums3.append(nums1[i]-nums2[i])
        def merge(left,right,mid):
            nonlocal n
            ans = 0
            l =left
            count = 0
            for i in range(mid+1,right+1):
                while l < mid+1 and nums3[i]+diff >= nums3[l]:
                    count +=1
                    l +=1
                ans +=count
            left_l = left
            right_l = mid+1
            res =[]
            while left_l< mid+1 and right_l <right+1:
                if nums3[left_l]>=nums3[right_l]:
                    res.append(nums3[right_l])
                    right_l+=1
                else:
                    res.append(nums3[left_l])
                    left_l+=1
            if left_l < mid+1:
                res+=nums3[left_l:mid+1]
            if right_l <right+1:
                res+=nums3[right_l:right+1]
            nums3[left:right+1] = res
            return ans
        def mergeSort(left,right):
            if left >= right:
                return 0
            mid = (left+right)//2
            leftVal = mergeSort(left,mid)
            rightVal =mergeSort(mid+1,right)
            mergeVal = merge(left,right,mid)
            return leftVal +rightVal + mergeVal
        return mergeSort(0,n-1)
