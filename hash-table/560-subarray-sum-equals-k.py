from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        curr = 0
        seen = {0: 1}
        for i in range(len(nums)):
            curr += nums[i]
            # case [0,0,1] -> check multiple times
            if (curr - k) in seen:
                count += seen[curr - k]
            seen[curr] = seen.get(curr, 0) + 1
        return count
