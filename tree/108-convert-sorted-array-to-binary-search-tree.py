# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        # create func build tree
        # build from l and r, the root will be the middle
        # left - mid - 1 will be the left of the root
        # mid + 1 - right will be the right of the root
        def build(l, r):
            # base case
            if l > r:
                return None
            mid = (l + r) // 2
            root = TreeNode(nums[mid])
            root.left = build(l, mid - 1)
            root.right = build(mid + 1, r)
            return root

        return build(0, len(nums) - 1)

        # Time: O(n)
        # Space: O(log n)
