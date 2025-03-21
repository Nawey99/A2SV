# Problem: Find Largest Value in Each Tree Row - https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        que = deque()
        if not root:
            return []
        que.append(root)
        res = []
        while que:
            n = len(que)
            ans = []
            Max = float(-inf)
            for i in range(n):
                node = que.popleft()
                Max= max(Max,node.val)
                if node.left:
                    que.append(node.left)   
                if node.right:
                    que.append(node.right)
            res.append(Max)
        return res