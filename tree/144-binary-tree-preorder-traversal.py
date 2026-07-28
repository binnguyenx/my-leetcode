from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        # root -> left -> right
        res = []
        stack = [root]
        while stack:
            # going root first
            curr = stack.pop()
            res.append(curr.val)
            # put the right into the stack first, and then take it later
            if curr.right:
                stack.append(curr.right)
            # put the left into the stack later, then take it first
            if curr.left:
                stack.append(curr.left)
        return res


class SolutionRecursive:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return (
            [root.val]
            + self.preorderTraversal(root.left)
            + self.preorderTraversal(root.right)
        )
