# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        # BST - the value is increasing
        # inorder dfs
        res = None
        count = 0

        def dfs(node):
            # we need to set nonlocal for 2 variables
            # because the ans can exist everywhere
            # base case
            nonlocal res, count
            if not node or res is not None:
                return

            # left - node - right
            dfs(node.left)
            count += 1
            if count == k:
                res = node.val
                return
            dfs(node.right)

        dfs(root)
        return res
