# Problem: House Robber III - https://leetcode.com/problems/house-robber-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        def dp(node,take):
            if not node:
                return 0
            if not take:
                return dp(node.right,not take)+dp(node.left, not take)
            else:
                if node not in memo:
                    memo[node] =  max((node.val + dp(node.right,not take)+dp(node.left, not take)), (dp(node.right,take)+dp(node.left,take)))
                return memo[node]
        return dp(root,True)