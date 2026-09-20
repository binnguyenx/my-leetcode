from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # the idea is generate the prefix sum first
        # then, checking if each prefix - k is seen or not,
        # if yes, count plus how many times that exists. if not skip
        # after, put each value of prefix in seen so we can use that later
        count = 0
        curr = 0
        # if subarray start from index 0, ex: [3] and k = 3
        seen = {0: 1}
        for i in range(len(nums)):
            curr += nums[i]
            if (curr - k) in seen:
                count += seen[curr - k]
            # put the curr in hash for the next time using
            seen[curr] = seen.get(curr, 0) + 1
        return count
