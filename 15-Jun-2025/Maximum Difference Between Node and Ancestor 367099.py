# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        Min = float("inf")
        Max = float("-inf")
        def dfs(node,curr_min,curr_max):
            if not node:
                return curr_max-curr_min
            curr_min = min(curr_min,node.val)
            curr_max = max(curr_max,node.val)
            return max(dfs(node.left,curr_min,curr_max),dfs(node.right,curr_min,curr_max))
        return dfs(root,root.val,root.val)
