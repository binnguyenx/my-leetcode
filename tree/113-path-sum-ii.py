# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def pathSum(
        self, root: TreeNode | None, targetSum: int
    ) -> list[list[int]]:
        res = []
        path = []

        # path is mutable, remaining is an integer
        def dfs(node, remaining):
            if not node:
                return

            path.append(node.val)
            remaining -= node.val

            # reached a leaf
            if not node.left and not node.right:
                if remaining == 0:
                    res.append(path.copy())

            dfs(node.left, remaining)
            dfs(node.right, remaining)
            path.pop()

        dfs(root, targetSum)
        return res
