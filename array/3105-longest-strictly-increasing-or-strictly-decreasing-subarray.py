from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        count_in = 1
        count_de = 1
        res = 1
        for i in range(len(nums) - 1):
            if nums[i + 1] > nums[i]:
                count_in += 1
                count_de = 1
            elif nums[i + 1] < nums[i]:
                count_de += 1
                count_in = 1
            else:
                count_de = 1
                count_in = 1
            res = max(count_in, count_de, res)
        return res
