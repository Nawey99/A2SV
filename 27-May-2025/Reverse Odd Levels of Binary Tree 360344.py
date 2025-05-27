# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        que = deque()
        i=0
        que.append(root)
        while que:
            temp =[]
            n = len(que)
            if i&1:
                for _ in range(n):
                    x = que.popleft()
                    temp.append(x.val)
                    que.append(x)
                temp = temp[::-1]
            for j in range(n):
                x = que.popleft()
                if temp:
                    x.val = temp[j]
                if x.left:
                    que.append(x.left)
                if x.right:
                    que.append(x.right)
            i+=1
        return root