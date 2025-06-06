# Problem: Count Nodes Equal to Average of Subtree - https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        count = 0
        def dfs(root):
            nonlocal count
            if not root:
                return (0,0)
            right_sum,right_count = dfs(root.right)
            left_sum,left_count = dfs(root.left)

            total_sum = left_sum + right_sum + root.val
            total_count = left_count + right_count + 1
            avg = total_sum // total_count
            if avg == root.val:
                count +=1
            return (total_sum, total_count)
        dfs(root)
        return count