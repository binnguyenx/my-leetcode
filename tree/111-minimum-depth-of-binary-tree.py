from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # root is leaf
        if not root.left and not root.right:
            return 1
        # no left child -> go right
        if not root.left:
            return 1 + self.minDepth(root.right)
        # no right child -> go left
        if not root.right:
            return 1 + self.minDepth(root.left)
        # both exist
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
