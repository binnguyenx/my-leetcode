from collections import deque
from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # use bfs, checking both tree at the same time
        queue = deque([(p, q)])
        while queue:
            node1, node2 = queue.popleft()
            # both none
            if not node1 and not node2:
                continue
            # node1 or node2 is none
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            # append left with left, right with right
            # T: O(n)
            # S: O(w) - the width of the tree
            queue.append((node1.left, node2.left))
            queue.append((node1.right, node2.right))
        return True
