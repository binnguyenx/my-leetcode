from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(curr):
            # edge case
            if not curr:
                return [True, 0]
            left = dfs(curr.left)
            right = dfs(curr.right)
            # 3 case that will turn to false, left not balance, right not balance, and tree not balance
            if left[0] == False:
                balanced = False
            elif right[0] == False:
                balanced = False
            elif abs(left[1] - right[1]) > 1:
                balanced = False
            else:
                balanced = True
            height = 1 + max(left[1], right[1])
            return [balanced, height]

        res = dfs(root)
        return res[0]
