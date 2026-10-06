from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # non decreasing: greater or equal to previous
        # left - add 1
        # right - add 1
        # left + 1 + right (nums[i-1] <= a <= nums[i+1])
        # left[i]: length of non decreasing end at i
        # right[i]: length of non decreasing start at i
        n = len(nums)
        # replace nums[i]
        # left - a - right
        # nums[i-1] <= nums[i+1]
        # yes - connect both
        # no - check left or right
        # edge case
        if n <= 2:
            return n
        # calculate left
        left = [1] * n
        for i in range(1, n):
            if nums[i - 1] <= nums[i]:
                left[i] = left[i - 1] + 1
            else:
                left[i] = 1
        # calculate right
        right = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                right[i] = right[i + 1] + 1
            else:
                right[i] = 1
        res = max(left)
        # replace the first
        res = max(res, 1 + right[1])
        # replace the last
        res = max(res, left[n - 2] + 1)
        for i in range(1, n - 1):
            # connect left
            res = max(res, left[i - 1] + 1)
            # connect right
            res = max(res, right[i + 1] + 1)
            # connect both
            if nums[i - 1] <= nums[i + 1]:
                res = max(res, left[i - 1] + 1 + right[i + 1])
        return res
