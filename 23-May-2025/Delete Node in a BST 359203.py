# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, node: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not node:
            return node
        
        if node.val == key:
            if not node.right and not node.left:
                return None
            if not node.right:
                return node.left
            if not node.left:
                return node.right
            slow = node
            fast = node.left
            while fast and fast.right:
                slow=fast
                fast = fast.right
            node.val = fast.val
            if slow == node:
                node.left = fast.left
            else:
                slow.right = fast.left
        elif node.val > key:
            node.left = self.deleteNode(node.left,key)
        else:
            node.right = self.deleteNode(node.right,key)
        return node