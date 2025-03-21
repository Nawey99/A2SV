# Problem: Convert Sorted Array to Binary Search Tree - https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left,right):
            if left >right:
                return
            mid = (left+right)//2
            right = helper(mid+1,right)
            left = helper(left, mid-1)
            return TreeNode(nums[mid],left,right)
        return helper(0,len(nums)-1)
