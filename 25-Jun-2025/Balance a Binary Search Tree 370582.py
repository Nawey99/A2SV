# Problem: Balance a Binary Search Tree - https://leetcode.com/problems/balance-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inord(node,nodes):
            if not node:
                return
            inord(node.left,nodes)
            nodes.append(node.val)
            inord(node.right,nodes)
        def buildtree(arr,start,end):
            if start>end:
                return
            mid = (start+end)//2

            ans = TreeNode(arr[mid])
            ans.left = buildtree(arr,start,mid-1)
            ans.right = buildtree(arr,mid+1,end)
            return ans
        arr = []
        inord(root,arr)
        n = len(arr)
        return buildtree(arr,0,n-1)
