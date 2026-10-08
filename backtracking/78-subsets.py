from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(start, curr):
            res.append(curr[:])
            for i in range(start, len(nums)):
                # choose
                curr.append(nums[i])
                # explore
                backtrack(i + 1, curr)
                # pop
                curr.pop()

        backtrack(0, [])
        return res
