from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # post order, going by left -> right -> root
        # so the stack must be root -> right -> left
        # we must track if the root have the children or not, if we clear their child, make the stack to true
        if not root:
            return []
        stack = [(root, False)]
        res = []
        while stack:
            node, visited = stack.pop()
            if node:
                # if visited turn to true, append to res
                if visited == True:
                    res.append(node.val)
                else:
                    # we haven't visit it, so false, and push it to the stack reversely
                    # we want left, right, root, so we push root, right, left
                    stack.append((node, True))
                    if node.right:
                        stack.append((node.right, False))
                    if node.left:
                        stack.append((node.left, False))
        return res


class SolutionRecursive:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return (
            self.postorderTraversal(root.left)
            + self.postorderTraversal(root.right)
            + [root.val]
        )
