from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefix sum + hashmap: count occurrences of each prefix sum
        count = 0
        prefix = 0
        seen = defaultdict(int)
        seen[0] = 1
        for num in nums:
            prefix += num
            # if (prefix - k) seen before, those subarrays sum to k
            count += seen[prefix - k]
            seen[prefix] += 1
        return count
