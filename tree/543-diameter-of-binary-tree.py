from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def dfs(curr):
            if not curr:
                return 0
            length_left = dfs(curr.left)
            length_right = dfs(curr.right)
            self.diameter = max(self.diameter, length_left + length_right)
            return 1 + max(length_left, length_right)

        dfs(root)
        return self.diameter
