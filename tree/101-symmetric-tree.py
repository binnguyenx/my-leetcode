from collections import deque
from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # edge case
        if not root:
            return True

        queue = deque([(root.left, root.right)])
        # node left - node right
        while queue:
            node1, node2 = queue.popleft()

            # both empty
            if not node1 and not node2:
                continue

            # one empty
            if not node2 or not node1:
                return False

            # dif values
            if node1.val != node2.val:
                return False

            queue.append((node1.left, node2.right))
            queue.append((node1.right, node2.left))

        return True
