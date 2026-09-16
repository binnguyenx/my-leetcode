# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def countNodes(self, root: TreeNode | None) -> int:
        # complete binary tree -> the last layer fills from left -> right

        # base case
        if not root:
            return 0

        left_height, right_height = 0, 0
        left = root
        right = root

        # perfect tree node is 2^h - 1
        # if not perfect, still recursion
        while left:
            left_height += 1
            left = left.left
        while right:
            right_height += 1
            right = right.right

        # if perfect
        if left_height == right_height:
            return 2**left_height - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

        # Complexity: h = O(logn)
        # in each h, need O(logn) for each level
