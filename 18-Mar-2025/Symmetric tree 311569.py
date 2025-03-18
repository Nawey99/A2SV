# Problem: Symmetric tree - https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        que = deque()
        que.append(root)
        while que:
            n = len(que)
            ans = []
            for i in range(n):
                node = que.popleft()
                if node:
                    que.append(node.left)   
                    que.append(node.right)
                    ans.append(node.val)
                else:
                    ans.append('x')
            if ans != ans[::-1]: return False
            print(ans)
        return True