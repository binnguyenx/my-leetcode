from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        # BFS tracks each node with its lower and upper bounds
        # left range: (lower, node.val)
        # right range: (node.val, upper)
        if not root:
            return True

        queue = deque([(root, -float("inf"), float("inf"))])
        while queue:
            node, lower, upper = queue.popleft()

            # the value must be strictly within the valid range
            if not (lower < node.val < upper):
                return False

            if node.left:
                queue.append((node.left, lower, node.val))
            if node.right:
                queue.append((node.right, node.val, upper))

        return True
