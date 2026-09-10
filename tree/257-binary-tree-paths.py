from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        # go straight to the leaf -> backtrack
        # dfs + backtracking
        def dfs(node, path):
            if not node:
                return
            # add current node into the path
            path.append(str(node.val))
            # checking leaf
            if not node.left and not node.right:
                res.append("->".join(path))
            else:
                dfs(node.left, path)
                dfs(node.right, path)
            # remove
            path.pop()

        dfs(root, [])
        return res
