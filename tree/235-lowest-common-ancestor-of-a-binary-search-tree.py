# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # lca is when they are splitting - left - root - right
        # edge case is example 2 - so just return if not both left or right
        curr = root
        while curr:
            # both left
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            # both right
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # if they split -> return curr
            else:
                return curr
