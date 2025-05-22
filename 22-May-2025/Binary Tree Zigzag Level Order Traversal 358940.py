# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        que =deque()
        que.append(root)
        ans = []
        flag = 0
        while que:
            temp = []
            n = len(que)
            for _ in range(n):
                x = que.popleft()
                temp.append(x.val)
                if x.left:
                    que.append(x.left)
                if x.right:
                    que.append(x.right)
            if flag == 0:
                ans.append(temp)
                flag = 1
            else:
                ans.append(temp[::-1])
                flag = 0
        return ans
        
